#!/usr/bin/env python3
"""FMC card <-> host compatibility engine.

Pure and importable. Given a *card* FMC pinout slot and a *host* FMC pinout slot
(both in the ``fmc_pinout`` schema shape), decide whether the card mates with
that host slot and explain why.

Design (see the FMC-compat architecture notes):

* **Closed-world.** A signal absent from a host slot is treated as NOT routed —
  never "unknown". Files with genuinely missing pins are a data-quality problem
  fixed by editing the file, not modelled here.
* **Two layers, one engine.** This module is the *mechanical* layer only. Vendor
  endorsement (relationships/fmc-mates) is composed on top by the build script.
* **Functional groups.** A card declares independent functional units (e.g. the
  four ports of a quad-RGMII Ethernet FMC) via ``slot.groups``. A group is
  satisfied when every signal it lists is routed on the host slot AND, if
  ``same_bank`` is set, all those signals share one host I/O bank. The verdict is
  COMPATIBLE (all groups satisfied), PARTIAL (some), or INCOMPATIBLE (none). A
  card with no groups is checked as one implicit all-or-nothing group.

INDETERMINATE is *not* produced here — it is the matrix-level state the build
driver emits when one side has no pinout file at all (so this function can't be
called for that pair).

Lives in the board-repo so the website build (scripts/build.py imports it from
the submodule) and the board-repo CI discrepancy guard share one copy, mirroring
json_from_md.py.
"""
from __future__ import annotations

import re

# A transceiver lane signal: DP<n>_C2M/M2C_P/N. The lane index groups the 4
# signals of one serial lane for min_lanes counting.
_DP_LANE = re.compile(r"^DP(\d+)_")

COMPATIBLE = "compatible"
PARTIAL = "partial"
INCOMPATIBLE = "incompatible"
INDETERMINATE = "indeterminate"  # matrix-level only; never returned by evaluate_slot

# Connector classes, ordered by pin superset. A card seats in any host whose
# connector is the same class or a richer one: an LPC card fits LPC/HPC/FMC+,
# an HPC card fits HPC/FMC+, an FMC+ card fits FMC+ only.
_CONNECTOR_RANK = {"lpc": 0, "hpc": 1, "fmcp": 2}


def host_superset(card_type: str, host_type: str) -> bool:
    """True if the host connector exposes at least the card's full pin region.

    NOT a seating gate. LPC/HPC/FMC+ share one Samtec connector shell (smaller
    classes are partially populated), so any card physically seats in any host —
    an HPC card in an LPC site simply gets the LPC-region pins. Whether it
    *works* is decided entirely by the signal-subset check below. This helper is
    informational only: it reports whether every pin region the card could use
    is present on the host (host class >= card class)."""
    c = _CONNECTOR_RANK.get((card_type or "").lower())
    h = _CONNECTOR_RANK.get((host_type or "").lower())
    if c is None or h is None:
        return False
    return h >= c


def _vadj_overlap(card_vadj, host_vadj):
    """Return True/False for VADJ-range overlap, or None when host VADJ unknown.

    Each arg is ``(min, max)`` or None. Card VADJ is required for a real check;
    host slot VADJ is frequently unpopulated, in which case we abstain (None)
    rather than fail — VADJ is entity data, separate from the closed-world pin
    rule.
    """
    if not card_vadj or not host_vadj:
        return None
    cmin, cmax = card_vadj
    hmin, hmax = host_vadj
    if None in (cmin, cmax, hmin, hmax):
        return None
    return cmin <= hmax and hmin <= cmax


def _implicit_groups(card_slot):
    """A card with no declared groups is one all-or-nothing group of every used signal."""
    return [{
        "name": "(all signals)",
        "signals": [s["signal"] for s in card_slot.get("signals", [])],
        "same_bank": False,
    }]


def evaluate_slot(card_slot, host_slot, *, card_vadj=None, host_vadj=None):
    """Evaluate one card slot against one host slot.

    ``card_slot`` / ``host_slot`` are ``fmc_pinout`` slot dicts. ``card_vadj`` /
    ``host_vadj`` are optional ``(min, max)`` tuples. Returns a result dict:

        {
          "verdict": COMPATIBLE | PARTIAL | INCOMPATIBLE,
          "connector": {"card", "host", "ok"},
          "vadj": {"card", "host", "ok"},        # ok is True/False/None
          "groups": [{"name", "satisfied", "missing", "same_bank", "banks"}],
          "satisfied": [group names], "unsatisfied": [group names],
          "summary": str,
          "reasons": [str, ...],
        }
    """
    card_type = card_slot.get("type")
    host_type = host_slot.get("type")
    reasons = []

    superset = host_superset(card_type, host_type)
    vadj_ok = _vadj_overlap(card_vadj, host_vadj)

    host_signals = {s["signal"] for s in host_slot.get("signals", [])}
    host_bank = {s["signal"]: s.get("bank") for s in host_slot.get("signals", [])}

    modeled = "groups" in card_slot
    groups = card_slot.get("groups") or _implicit_groups(card_slot)
    group_results = []
    for g in groups:
        sigs = g.get("signals", [])
        same_bank = bool(g.get("same_bank"))
        min_lanes = g.get("min_lanes")
        gr = {"name": g.get("name", "(group)"), "same_bank": same_bank, "banks": None,
              "missing": [], "lanes_present": None, "lanes_total": None}
        if min_lanes:
            # Multi-lane transceiver slot (PCIe / QSFP). DP signals are serial
            # lanes (4 signals per DP index); non-DP signals are required control.
            # The slot functions at >= min_lanes lanes, degrading in width — so
            # the group is satisfied with as few as min_lanes lanes routed, and
            # we report how many of the full set are available.
            lanes, non_dp = {}, []
            for s in sigs:
                m = _DP_LANE.match(s)
                if m:
                    lanes.setdefault(int(m.group(1)), []).append(s)
                else:
                    non_dp.append(s)
            present_lanes = [i for i, ls in lanes.items() if all(x in host_signals for x in ls)]
            non_dp_missing = [s for s in non_dp if s not in host_signals]
            gr["lanes_present"] = len(present_lanes)
            gr["lanes_total"] = len(lanes)
            gr["missing"] = non_dp_missing
            gr["satisfied"] = len(present_lanes) >= min_lanes and not non_dp_missing
        else:
            missing = [s for s in sigs if s not in host_signals]
            present = not missing
            bank_ok = True
            if present and same_bank:
                gr["banks"] = sorted({host_bank.get(s) for s in sigs}, key=lambda b: (b is None, b))
                bank_ok = len(gr["banks"]) == 1 and gr["banks"][0] is not None
            gr["missing"] = missing
            gr["satisfied"] = present and bank_ok
        group_results.append(gr)

    def reduced(g):  # satisfied but at less than full lane width
        return bool(g["lanes_total"]) and g["satisfied"] and g["lanes_present"] < g["lanes_total"]

    def glabel(g):
        return (f"{g['name']} (x{g['lanes_present']} of x{g['lanes_total']})"
                if reduced(g) else g["name"])

    sat = [g["name"] for g in group_results if g["satisfied"]]
    unsat = [g["name"] for g in group_results if not g["satisfied"]]
    n = len(group_results)

    if len(sat) == n:
        signal_verdict = COMPATIBLE
    elif len(sat) == 0:
        signal_verdict = INCOMPATIBLE
    else:
        signal_verdict = PARTIAL

    # `verdict` reports PIN FIT only. VADJ is an independent axis (see `vadj`):
    # the connector class is not a gate (seating is universal) and VADJ is
    # reported separately so the UI can present pins / VADJ / endorsement as
    # orthogonal checks. A consumer wanting net usability ANDs them: works =
    # verdict in {compatible, partial} AND vadj.ok is not False.
    verdict = signal_verdict
    if vadj_ok is False:
        reasons.append(f"VADJ ranges do not overlap (card {card_vadj} V, host {host_vadj} V).")

    # Human-readable group summary (lane width folded into satisfied-group labels).
    sat_groups = [g for g in group_results if g["satisfied"]]
    if modeled and n > 1:
        if verdict == COMPATIBLE:
            red = [glabel(g) for g in sat_groups if reduced(g)]
            summary = f"All {n} groups" + (" — reduced: " + ", ".join(red) if red else "")
        elif verdict == PARTIAL:
            summary = f"{len(sat)} of {n}: " + ", ".join(glabel(g) for g in sat_groups)
        else:
            summary = "No groups satisfied"
    elif modeled and n == 1 and reduced(group_results[0]):
        g0 = group_results[0]
        summary = f"x{g0['lanes_present']} of x{g0['lanes_total']} lanes"
    else:
        summary = {COMPATIBLE: "Pin-compatible", PARTIAL: "Partial",
                   INCOMPATIBLE: "Incompatible"}[verdict]

    for g in group_results:
        if g["satisfied"]:
            if reduced(g):
                reasons.append(f"{g['name']}: only {g['lanes_present']} of {g['lanes_total']} "
                               f"lanes routed (operates at x{g['lanes_present']}).")
        elif g["lanes_total"]:
            if g["missing"]:
                reasons.append(f"{g['name']}: control signals not routed "
                               f"(e.g. {', '.join(g['missing'][:3])}).")
            else:
                reasons.append(f"{g['name']}: no transceiver lanes routed (0 of {g['lanes_total']}).")
        elif g["missing"]:
            reasons.append(f"{g['name']}: not routed ({len(g['missing'])} signal(s) missing, "
                           f"e.g. {', '.join(g['missing'][:3])}).")
        elif g["same_bank"]:
            reasons.append(f"{g['name']}: signals split across host banks {g['banks']} "
                           f"(must share one bank).")
    if vadj_ok is None and card_vadj:
        reasons.append("VADJ overlap not verified (host slot VADJ unspecified).")

    return {
        "verdict": verdict,
        "modeled": modeled,
        "connector": {"card": card_type, "host": host_type, "host_superset": superset},
        "vadj": {"card": list(card_vadj) if card_vadj else None,
                 "host": list(host_vadj) if host_vadj else None, "ok": vadj_ok},
        "groups": group_results,
        "satisfied": sat,
        "unsatisfied": unsat,
        "summary": summary,
        "reasons": reasons,
    }


def card_vadj_of(rec):
    """``(min, max)`` VADJ tuple from an fmc_card entity record, or None."""
    if rec and rec.get("vadj_min") is not None:
        return (rec["vadj_min"], rec["vadj_max"])
    return None


def host_slot_vadj_of(rec):
    """``{slot: (min, max)}`` from a host entity's expansion.fmc[], where given."""
    out = {}
    for s in ((rec or {}).get("expansion", {}).get("fmc") or []):
        if s.get("vadj_min") is not None:
            out[s["slot"]] = (s["vadj_min"], s["vadj_max"])
    return out


def find_discrepancies(card_pinouts, host_pinouts, fmc_mates, fmc_cards, host_lookups):
    """Vendor-asserted edges the mechanical engine refutes.

    ``card_pinouts``  {card_mpn: pinout_doc}
    ``host_pinouts``  {(host_type, host_mpn): pinout_doc}
    ``fmc_mates``     iterable of edge dicts (fmc_card, host_type, host, target_slot)
    ``fmc_cards``     {mpn: entity_record}      (for card VADJ)
    ``host_lookups``  {host_type: {mpn: record}} (for host slot VADJ)

    Yields ``(severity, card, host_type, host, slot, why)``. severity is
    ``"hard"`` when a fully-modeled card disagrees (a real data bug — the engine
    should be trusted) or ``"soft"`` when an implicit-only card disagrees (the
    card lacks functional groups, so the mismatch is likely the card model, not
    the data). A pair with no pinout on a side is skipped (indeterminate).
    """
    out = []
    for rel in fmc_mates:
        cm, htype, hm, slot = rel["fmc_card"], rel["host_type"], rel["host"], rel.get("target_slot")
        cdoc, hdoc = card_pinouts.get(cm), host_pinouts.get((htype, hm))
        if cdoc is None or hdoc is None:
            continue
        hslot = host_slot_of(hdoc, slot)
        if hslot is None:
            continue
        r = evaluate_slot(
            card_slot_of(cdoc), hslot,
            card_vadj=card_vadj_of(fmc_cards.get(cm)),
            host_vadj=host_slot_vadj_of(host_lookups.get(htype, {}).get(hm)).get(slot),
        )
        if r["verdict"] == INCOMPATIBLE:
            why = r["reasons"][0] if r["reasons"] else r["summary"]
            out.append(("hard" if r["modeled"] else "soft", cm, htype, hm, slot, why))
    return out


def card_slot_of(card_doc):
    """A card pinout has exactly one slot (its single edge connector)."""
    return card_doc["slots"][0]


def host_slot_of(host_doc, slot_name):
    """Return the named slot from a host pinout doc, or None."""
    for s in host_doc.get("slots", []):
        if s.get("slot") == slot_name:
            return s
    return None


# --------------------------------------------------------------------------
# Self-test / golden fixtures. Run:  python scripts/fmc_compat.py
# Reproduces the hand-written fmc-mates caveats from pin data alone.
# --------------------------------------------------------------------------
def _selftest():
    import json, os, sys
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def load(rel):
        with open(os.path.join(root, rel), encoding="utf-8") as f:
            return json.load(f)

    op031 = card_slot_of(load("fmc-pinouts/fmc-cards/opsero/OP031-1V8.json"))
    op063 = card_slot_of(load("fmc-pinouts/fmc-cards/opsero/OP063.json"))
    H = {mpn: load(f"fmc-pinouts/boards/amd-xilinx/{mpn}.json")
         for mpn in ("ZCU102", "ZCU106", "ZCU104", "KCU105", "KC705")}

    # (label, card_slot, host, slot, verdict, expected_satisfied|None, summary_substr|None)
    cases = [
        # RGMII same_bank fixtures — reproduce the vendor "ports 0,1 only" caveat.
        ("OP031 x ZCU102 HPC0", op031, "ZCU102", "HPC0", COMPATIBLE, None, None),
        ("OP031 x ZCU102 HPC1", op031, "ZCU102", "HPC1", PARTIAL, {"Port 0", "Port 1"}, None),
        ("OP031 x ZCU106 HPC0", op031, "ZCU106", "HPC0", COMPATIBLE, None, None),
        ("OP031 x ZCU106 HPC1", op031, "ZCU106", "HPC1", PARTIAL, {"Port 0", "Port 1"}, None),
        # min_lanes fixtures — PCIe SSD slots degrade in width.
        ("OP063 x KCU105 HPC (8 lanes)", op063, "KCU105", "HPC", COMPATIBLE, None, None),
        ("OP063 x KC705 LPC (1 lane)", op063, "KC705", "LPC", PARTIAL, {"SSD Slot 1"}, "x1 of x4"),
        ("OP063 x ZCU104 LPC (1 lane)", op063, "ZCU104", "LPC", PARTIAL, {"SSD Slot 1"}, "x1 of x4"),
    ]
    failures = 0
    for label, cslot, hm, slot_name, exp_v, exp_sat, substr in cases:
        r = evaluate_slot(cslot, host_slot_of(H[hm], slot_name), card_vadj=(1.8, 1.8))
        ok = (r["verdict"] == exp_v
              and (exp_sat is None or set(r["satisfied"]) == exp_sat)
              and (substr is None or substr in r["summary"]))
        failures += not ok
        print(f"[{'ok ' if ok else 'FAIL'}] {label:32} -> {r['verdict']:12} {r['summary']}")
        if not ok:
            print(f"        expected {exp_v} sat={exp_sat} substr={substr!r}; reasons: {r['reasons']}")
    print(f"\n{failures} fixture failure(s)" if failures else "\nall fixtures pass")
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    _selftest()
