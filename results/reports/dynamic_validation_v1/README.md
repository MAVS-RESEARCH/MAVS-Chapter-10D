# MAVS Chapter 10D Dynamic Validation V1

## Execution Status

- Full minimum execution status: `complete`.
- Required trace records: `383200`.
- Aggregated trace records: `383200`.
- Episode rows: `2530`.
- Dynamic environment families represented: `5`.
- Method ids represented: `36`.
- Failure cards generated: `12161`.
- Weighted trace completeness: `1.0000`.
- Weighted audit-trace completeness: `1.0000`.

## Minimum Coverage

| Experiment | Scope | Required Records | Actual Records | Coverage | Status |
| --- | --- | ---: | ---: | ---: | --- |
| `E1` | Dynamic corruption | 21600 | 21600 | 1.0000 | `complete` |
| `E2` | Correlated failure | 16000 | 16000 | 1.0000 | `complete` |
| `E3` | Governance baseline comparison | 100800 | 100800 | 1.0000 | `complete` |
| `E4` | Ablation study | 230400 | 230400 | 1.0000 | `complete` |
| `E5` | Stress schedule sweep | 14400 | 14400 | 1.0000 | `complete` |

## MAVS-GC Focus Rows

| experiment_code | environment_family | method_id | seed_count | step_count | mean_reward | unsafe_acceptance_rate | false_rejection_rate | escalation_rate | correlation_collapse_sensitivity |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | synthetic_ops | mavs_gc_E1_synthetic_ops | 30 | 7200 | 0.8571 | 0.0000 | 0.1650 | 0.0000 | -0.1720 |
| E1 | text_safety_stream | mavs_gc_E1_text_safety | 30 | 7200 | 0.9130 | 0.0000 | 0.1240 | 0.0000 | 0.9130 |
| E1 | tool_use_security | mavs_gc_E1_tool_use | 30 | 7200 | 0.9575 | 0.0000 | 0.0630 | 0.0000 | 0.9575 |
| E2 | correlated_representation_collapse | mavs_gc_correlated_final | 50 | 8000 | 0.0250 | 0.0000 | 1.0000 | 0.0000 | -1.0000 |
| E2 | multi_agent_operations | mavs_gc_E2_multi_agent | 50 | 8000 | 0.9347 | 0.0000 | 0.1003 | 0.0000 | 0.1742 |
| E3 | synthetic_ops | mavs_gc_full_final | 20 | 2400 | 0.8578 | 0.0000 | 0.1804 | 0.0000 | -0.1872 |
| E3 | text_safety_stream | mavs_gc_full_final | 20 | 2400 | 0.9932 | 0.0000 | 0.0074 | 0.0000 | 0.4062 |
| E3 | tool_use_security | mavs_gc_full_final | 20 | 2400 | 0.8974 | 0.0000 | 0.1703 | 0.0000 | 0.8974 |
| E4 | synthetic_ops | mavs_gc_accept_reject_only_no_escalation | 30 | 4800 | 0.8214 | 0.0000 | 0.2521 | 0.0000 | -0.2625 |
| E4 | synthetic_ops | mavs_gc_delayed_threshold | 30 | 4800 | 0.8214 | 0.0000 | 0.2521 | 0.0000 | -0.2625 |
| E4 | synthetic_ops | mavs_gc_fixed_severity | 30 | 4800 | 1.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| E4 | synthetic_ops | mavs_gc_fixed_threshold | 30 | 4800 | 0.8214 | 0.0000 | 0.2521 | 0.0000 | -0.2625 |
| E4 | synthetic_ops | mavs_gc_full_mavs_gc | 30 | 4800 | 0.8214 | 0.0000 | 0.2521 | 0.0000 | -0.2625 |
| E4 | synthetic_ops | mavs_gc_heterogeneous_specialists | 30 | 4800 | 0.8214 | 0.0000 | 0.2521 | 0.0000 | -0.2625 |
| E4 | synthetic_ops | mavs_gc_homogeneous_specialists | 30 | 4800 | 0.8214 | 0.0000 | 0.2521 | 0.0000 | -0.2625 |
| E4 | synthetic_ops | mavs_gc_no_diagnostics | 30 | 4800 | 1.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| E4 | synthetic_ops | mavs_gc_no_escalation | 30 | 4800 | 0.8214 | 0.0000 | 0.2521 | 0.0000 | -0.2625 |
| E4 | synthetic_ops | mavs_gc_no_severity | 30 | 4800 | 1.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| E4 | synthetic_ops | mavs_gc_noisy_severity | 30 | 4800 | 0.8245 | 0.0000 | 0.2411 | 0.0063 | -0.2579 |
| E4 | synthetic_ops | mavs_gc_over_sensitive_threshold | 30 | 4800 | 0.8214 | 0.0000 | 0.2521 | 0.0000 | -0.2625 |
| ... | 38 additional rows in summary_metrics.csv |  |  |  |  |  |  |  |  |

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
- Failure card count: `12161`
- Full detail remains in `summary_metrics.csv`, `summary_metrics.md`, and the failure-card directory.

## Negative Results And Collapse Cases

- Unsafe-acceptance negative-result rows: `20`.
- Highest UAR rows:

| experiment_code | environment_family | method_id | unsafe_acceptance_rate | false_rejection_rate | mean_reward | step_count |
| --- | --- | --- | --- | --- | --- | --- |
| E3 | synthetic_ops | disagreement_gate_final | 1.0000 | 0.0000 | -0.1837 | 2400 |
| E3 | synthetic_ops | always_accept_sanity | 1.0000 | 0.0000 | -0.1087 | 2400 |
| E3 | synthetic_ops | confidence_gate_final | 1.0000 | 0.0000 | -0.1087 | 2400 |
| E3 | synthetic_ops | validator_stack_final | 1.0000 | 0.0000 | -0.1087 | 2400 |
| E3 | tool_use_security | always_accept_sanity | 1.0000 | 0.0000 | -0.0358 | 2400 |
| E3 | tool_use_security | confidence_gate_final | 1.0000 | 0.0000 | -0.0358 | 2400 |
| E3 | tool_use_security | disagreement_gate_final | 1.0000 | 0.0000 | -0.0358 | 2400 |
| E3 | text_safety_stream | disagreement_gate_final | 1.0000 | 0.0000 | 0.4600 | 2400 |
| E3 | text_safety_stream | always_accept_sanity | 1.0000 | 0.0000 | 0.4625 | 2400 |
| E3 | text_safety_stream | confidence_gate_final | 1.0000 | 0.0000 | 0.4625 | 2400 |
| E3 | text_safety_stream | validator_stack_final | 0.9426 | 0.0000 | 0.4933 | 2400 |
| E3 | tool_use_security | conformal_adaptive_final | 0.6484 | 0.0000 | 0.2549 | 2400 |
| ... | 8 additional rows in summary_metrics.csv |  |  |  |  |  |

- Positive correlated-collapse sensitivity rows: `69`.
- Largest reward drops under shared/correlated conditions:

| experiment_code | environment_family | method_id | independent_mean_reward | shared_failure_mean_reward | correlation_collapse_sensitivity | step_count |
| --- | --- | --- | --- | --- | --- | --- |
| E3 | synthetic_ops | always_accept_sanity | 0.4899 | -2.0000 | 2.4899 | 2400 |
| E3 | synthetic_ops | confidence_gate_final | 0.4899 | -2.0000 | 2.4899 | 2400 |
| E3 | synthetic_ops | validator_stack_final | 0.4899 | -2.0000 | 2.4899 | 2400 |
| E3 | synthetic_ops | disagreement_gate_final | 0.3911 | -2.0000 | 2.3911 | 2400 |
| E3 | synthetic_ops | conformal_adaptive_final | 0.8749 | -1.1434 | 2.0183 | 2400 |
| E3 | synthetic_ops | conformal_static_final | 1.0000 | -0.4610 | 1.4610 | 2400 |
| E4 | tool_use_security | mavs_gc_single_diagnostic_only | 1.0000 | 0.0000 | 1.0000 | 4800 |
| E5 | tool_use_security | mavs_gc_stress_final | 1.0000 | 0.0000 | 1.0000 | 7200 |
| E3 | tool_use_security | policy_rails_final | 1.0000 | 0.0000 | 1.0000 | 2400 |
| E4 | text_safety_stream | mavs_gc_fixed_severity | 1.0000 | 0.0000 | 1.0000 | 4800 |
| E4 | tool_use_security | mavs_gc_no_diagnostics | 1.0000 | 0.0000 | 1.0000 | 4800 |
| E4 | text_safety_stream | mavs_gc_no_diagnostics | 1.0000 | 0.0000 | 1.0000 | 4800 |
| ... | 57 additional rows in summary_metrics.csv |  |  |  |  |  |

## Claim Limitations

- No frontier-model claim.
- No industrial-scale claim.
- No universal robustness claim.
- No proof that MAVS solves correlated failure.
- No claim that MAVS beats all governance methods.
