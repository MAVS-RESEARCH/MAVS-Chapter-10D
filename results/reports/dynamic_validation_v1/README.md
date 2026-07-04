# MAVS Chapter 10D Dynamic Validation V1

## Reproduction Commands

```bash
python scripts/run_experiment.py --config configs/experiments/correlated_failure.yaml
python scripts/run_suite.py --suite configs/suites/dynamic_governance_v1.yaml
python scripts/aggregate_results.py --input results/raw --out results/processed/summary.parquet
python scripts/make_failure_cards.py --input results/raw --out results/reports/dynamic_validation_v1/failure_cards
python scripts/make_report.py --summary results/processed/summary.parquet --out results/reports/dynamic_validation_v1
```

## Scope

This report evaluates dynamic governance behavior from reproducible MAVS Chapter 10D traces. No training is performed during final execution; any trained model path must load already frozen Phase 5 artifacts only.

## Produced Artifacts

- Summary CSV: `results\reports\dynamic_validation_v1\summary_metrics.csv`
- Summary Markdown: `results\reports\dynamic_validation_v1\summary_metrics.md`
- Figures: `C:\Users\Saif malik\MAVS-Ch10D\results\figures\unsafe_acceptance_rate.svg, C:\Users\Saif malik\MAVS-Ch10D\results\figures\mean_reward.svg`
- Failure card count: `4`

## Negative Results And Collapse Cases

- `always_accept_sanity` on `text_safety_stream` has UAR `1.0000`.
- `confidence_gate_final` on `text_safety_stream` has UAR `1.0000`.
- `disagreement_gate_final` on `text_safety_stream` has UAR `1.0000`.
- `validator_stack_final` on `text_safety_stream` has UAR `1.0000`.

- `mavs_gc_accept_reject_only_no_escalation` sensitivity `1.0000` in `synthetic_ops`.
- `mavs_gc_delayed_threshold` sensitivity `1.0000` in `synthetic_ops`.
- `mavs_gc_fixed_severity` sensitivity `1.0000` in `synthetic_ops`.
- `mavs_gc_fixed_threshold` sensitivity `1.0000` in `synthetic_ops`.
- `mavs_gc_full_mavs_gc` sensitivity `1.0000` in `synthetic_ops`.
- `mavs_gc_heterogeneous_specialists` sensitivity `1.0000` in `synthetic_ops`.
- `mavs_gc_homogeneous_specialists` sensitivity `1.0000` in `synthetic_ops`.
- `mavs_gc_no_diagnostics` sensitivity `1.0000` in `synthetic_ops`.
- `mavs_gc_no_escalation` sensitivity `1.0000` in `synthetic_ops`.
- `mavs_gc_no_severity` sensitivity `1.0000` in `synthetic_ops`.
- `mavs_gc_noisy_severity` sensitivity `1.0000` in `synthetic_ops`.
- `mavs_gc_over_sensitive_threshold` sensitivity `1.0000` in `synthetic_ops`.
- `mavs_gc_randomized_diagnostic` sensitivity `0.1875` in `synthetic_ops`.
- `mavs_gc_reject_only_fallback` sensitivity `1.0000` in `synthetic_ops`.
- `mavs_gc_shared_representation` sensitivity `1.0000` in `synthetic_ops`.
- `mavs_gc_single_diagnostic_only` sensitivity `1.0000` in `synthetic_ops`.
- `mavs_gc_accept_reject_only_no_escalation` sensitivity `1.0000` in `text_safety_stream`.
- `mavs_gc_delayed_threshold` sensitivity `1.0000` in `text_safety_stream`.
- `mavs_gc_fixed_severity` sensitivity `1.0000` in `text_safety_stream`.
- `mavs_gc_fixed_threshold` sensitivity `1.0000` in `text_safety_stream`.
- `mavs_gc_full_mavs_gc` sensitivity `1.0000` in `text_safety_stream`.
- `mavs_gc_heterogeneous_specialists` sensitivity `1.0000` in `text_safety_stream`.
- `mavs_gc_homogeneous_specialists` sensitivity `1.0000` in `text_safety_stream`.
- `mavs_gc_no_diagnostics` sensitivity `1.0000` in `text_safety_stream`.
- `mavs_gc_no_escalation` sensitivity `1.0000` in `text_safety_stream`.
- `mavs_gc_no_severity` sensitivity `1.0000` in `text_safety_stream`.
- `mavs_gc_noisy_severity` sensitivity `1.0000` in `text_safety_stream`.
- `mavs_gc_over_sensitive_threshold` sensitivity `1.0000` in `text_safety_stream`.
- `mavs_gc_randomized_diagnostic` sensitivity `0.5000` in `text_safety_stream`.
- `mavs_gc_reject_only_fallback` sensitivity `1.0000` in `text_safety_stream`.
- `mavs_gc_shared_representation` sensitivity `1.0000` in `text_safety_stream`.
- `mavs_gc_single_diagnostic_only` sensitivity `1.0000` in `text_safety_stream`.
- `mavs_gc_accept_reject_only_no_escalation` sensitivity `1.0000` in `tool_use_security`.
- `mavs_gc_delayed_threshold` sensitivity `1.0000` in `tool_use_security`.
- `mavs_gc_fixed_severity` sensitivity `1.0000` in `tool_use_security`.
- `mavs_gc_fixed_threshold` sensitivity `1.0000` in `tool_use_security`.
- `mavs_gc_full_mavs_gc` sensitivity `1.0000` in `tool_use_security`.
- `mavs_gc_heterogeneous_specialists` sensitivity `1.0000` in `tool_use_security`.
- `mavs_gc_homogeneous_specialists` sensitivity `1.0000` in `tool_use_security`.
- `mavs_gc_no_diagnostics` sensitivity `1.0000` in `tool_use_security`.
- `mavs_gc_no_escalation` sensitivity `1.0000` in `tool_use_security`.
- `mavs_gc_no_severity` sensitivity `1.0000` in `tool_use_security`.
- `mavs_gc_noisy_severity` sensitivity `1.0000` in `tool_use_security`.
- `mavs_gc_over_sensitive_threshold` sensitivity `1.0000` in `tool_use_security`.
- `mavs_gc_randomized_diagnostic` sensitivity `0.5000` in `tool_use_security`.
- `mavs_gc_reject_only_fallback` sensitivity `1.0000` in `tool_use_security`.
- `mavs_gc_shared_representation` sensitivity `1.0000` in `tool_use_security`.
- `mavs_gc_single_diagnostic_only` sensitivity `1.0000` in `tool_use_security`.
- `mavs_gc_E2_multi_agent` sensitivity `1.0000` in `multi_agent_operations`.
- `mavs_gc_E1_synthetic_ops` sensitivity `1.0000` in `synthetic_ops`.
- `mavs_gc_E1_text_safety` sensitivity `1.0000` in `text_safety_stream`.
- `mavs_gc_E1_tool_use` sensitivity `1.0000` in `tool_use_security`.
- `always_accept_sanity` sensitivity `1.0000` in `synthetic_ops`.
- `confidence_gate_final` sensitivity `1.0000` in `synthetic_ops`.
- `conformal_adaptive_final` sensitivity `1.0000` in `synthetic_ops`.
- `conformal_static_final` sensitivity `1.0000` in `synthetic_ops`.
- `critique_revise_final` sensitivity `1.0000` in `synthetic_ops`.
- `debate_final` sensitivity `1.0000` in `synthetic_ops`.
- `disagreement_gate_final` sensitivity `1.0000` in `synthetic_ops`.
- `judge_final` sensitivity `1.0000` in `synthetic_ops`.
- `mavs_gc_full_final` sensitivity `1.0000` in `synthetic_ops`.
- `policy_rails_final` sensitivity `1.0000` in `synthetic_ops`.
- `reject_option_final` sensitivity `1.0000` in `synthetic_ops`.
- `self_consistency_final` sensitivity `1.0000` in `synthetic_ops`.
- `validator_stack_final` sensitivity `1.0000` in `synthetic_ops`.
- `always_accept_sanity` sensitivity `0.5000` in `text_safety_stream`.
- `always_reject_sanity` sensitivity `0.0625` in `text_safety_stream`.
- `confidence_gate_final` sensitivity `0.5000` in `text_safety_stream`.
- `conformal_adaptive_final` sensitivity `1.0000` in `text_safety_stream`.
- `conformal_static_final` sensitivity `1.0000` in `text_safety_stream`.
- `critique_revise_final` sensitivity `1.0000` in `text_safety_stream`.
- `debate_final` sensitivity `1.0000` in `text_safety_stream`.
- `disagreement_gate_final` sensitivity `0.5000` in `text_safety_stream`.
- `judge_final` sensitivity `1.0000` in `text_safety_stream`.
- `mavs_gc_full_final` sensitivity `1.0000` in `text_safety_stream`.
- `policy_rails_final` sensitivity `1.0000` in `text_safety_stream`.
- `reject_option_final` sensitivity `1.0000` in `text_safety_stream`.
- `self_consistency_final` sensitivity `1.0000` in `text_safety_stream`.
- `validator_stack_final` sensitivity `0.5000` in `text_safety_stream`.
- `always_accept_sanity` sensitivity `1.0000` in `tool_use_security`.
- `confidence_gate_final` sensitivity `1.0000` in `tool_use_security`.
- `conformal_adaptive_final` sensitivity `1.0000` in `tool_use_security`.
- `conformal_static_final` sensitivity `1.0000` in `tool_use_security`.
- `critique_revise_final` sensitivity `1.0000` in `tool_use_security`.
- `debate_final` sensitivity `1.0000` in `tool_use_security`.
- `disagreement_gate_final` sensitivity `1.0000` in `tool_use_security`.
- `judge_final` sensitivity `1.0000` in `tool_use_security`.
- `mavs_gc_full_final` sensitivity `1.0000` in `tool_use_security`.
- `policy_rails_final` sensitivity `1.0000` in `tool_use_security`.
- `reject_option_final` sensitivity `1.0000` in `tool_use_security`.
- `self_consistency_final` sensitivity `1.0000` in `tool_use_security`.
- `validator_stack_final` sensitivity `1.0000` in `tool_use_security`.
- `mavs_gc_stress_final` sensitivity `1.0000` in `synthetic_ops`.
- `mavs_gc_stress_final` sensitivity `1.0000` in `tool_use_security`.

## Claim Limitations

- No frontier-model claim.
- No industrial-scale claim.
- No universal robustness claim.
- No proof that MAVS solves correlated failure.
- No claim that MAVS beats all governance methods.
