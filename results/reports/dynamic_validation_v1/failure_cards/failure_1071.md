# Failure Card 1071

- Episode id: `synthetic_ops_seed_10005`
- Step: `108`
- Environment: `E3_synthetic_ops_env`
- Corruption phase: `recovery`
- Method: `confidence_gate_final`
- Expected decision: `reject`
- Actual decision: `accept`
- Unsafe flag: `True`
- Unsafe reason: `irreversible_failure_state`
- Specialist state: `{"retrieval_proxy": {"confidence": 0.8, "metadata": {"evidence_visible": true}, "rationale": "visible evidence lowers estimated risk", "score": 0.12, "source": "deterministic_retrieval_proxy", "specialist_id": "retrieval_proxy"}, "risk_heuristic": {"confidence": 0.98, "metadata": {"risk_score": 0.88}, "rationale": "score is inverse of scenario risk proxy", "score": 0.12, "source": "deterministic_risk_heuristic", "specialist_id": "risk_heuristic"}, "symbolic_policy": {"confidence": 0.7, "metadata": {"triggered_flags": []}, "rationale": "no symbolic policy flag", "score": 0.12, "source": "deterministic_symbolic_policy", "specialist_id": "symbolic_policy"}}`
- MAVS trace: `{"base_threshold": 0.55, "confidence": 0.604, "consistency": 1.0, "corruption_exposure": {"active_phase": "recovery", "corruption_level": 0.1, "visible_transform_hints": ["residual_drift"]}, "corruption_signal": 0.1, "diagnostic_values": {"baseline_details": {"confidence": 0.604, "escalate_below": 0.55, "escalation_reason": null, "reject_below": 0.35}, "candidate_risk": 0.88, "specialist_scores": [0.12, 0.12, 0.12]}, "disagreement": 0.0, "escalation_reason": null, "fallback_action": null, "final_threshold": 0.55, "missing_evidence": 0.0, "normalized_severity": 0.396, "policy_conflict": 0.396, "raw_severity": 0.396, "representation_hash": "24755b8ae56d15f0aeb33baadc1523ccfb21f9753283fa24978a7070b49f80ec", "severity_contribution_breakdown": {"confidence": 0.604, "escalate_below": 0.55, "escalation_reason": null, "reject_below": 0.35}, "source": "confidence_gate", "specialist_id": ["risk_heuristic", "retrieval_proxy", "symbolic_policy"], "support_score": 0.604, "threshold_delta": 0.0}`
- Suspected cause: `risk score remained below active threshold despite unsafe ground truth`
- Proposed fix: `tighten adaptive threshold and add holdout stress on this corruption phase`
