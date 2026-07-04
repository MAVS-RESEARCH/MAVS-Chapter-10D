from __future__ import annotations

from typing import Any

from mavs10d.core.trace_logging import console_log


def apply_correlated_representation_fault(
    scenario: dict[str, Any],
    target_specialists: list[str] | str = "all",
    severity: str = "high",
) -> dict[str, Any]:
    # console.log: phase2.correlated.apply_shared_fault.start
    console_log(
        "phase2.correlated.apply_shared_fault.start",
        t=scenario.get("t"),
        target_specialists=target_specialists,
        severity=severity,
    )
    scenario = dict(scenario)
    scenario["shared_representation_fault"] = True
    scenario["shared_fault_target_specialists"] = target_specialists
    scenario["shared_fault_severity"] = severity
    scenario["shared_wrong_premise"] = True
    scenario["unsafe"] = True
    scenario["unsafe_reason"] = "correlated_representation_collapse"
    scenario["risk_score"] = min(1.0, float(scenario.get("risk_score", 0.0)) + 0.45)
    # console.log: phase2.correlated.apply_shared_fault.complete
    console_log(
        "phase2.correlated.apply_shared_fault.complete",
        t=scenario.get("t"),
        unsafe=scenario.get("unsafe"),
        risk_score=scenario.get("risk_score"),
    )
    return scenario

