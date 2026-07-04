# MAVS Chapter 10D Work Plan

## Purpose

This repository implements Chapter 10D: `MAVS_GC_Dynamic_Validation_and_Baseline_Comparison_Plan`. The practical goal is to upgrade the MAVS-GC validation program from bounded static benchmarks into a dynamic governance benchmark suite.

The benchmark must test MAVS-GC and modern baselines under sequential, non-stationary, adversarial, and correlated-failure conditions. It must not claim frontier-model industrial validation. It must claim only what the evidence supports: whether MAVS-GC behaves better than contemporary governance alternatives in dynamic, reproducible, auditable environments.

The current repository was cloned from `https://github.com/MAVS-RESEARCH/MAVS-Chapter-10D` and initially contains only `LICENSE`. This work plan therefore treats the repository as a new implementation scaffold for Chapter 10D while preserving compatibility with the Chapter 10A-v2 architecture described in the source plan.

## Source Documents Used

- `C:/Users/Saif malik/Downloads/Mavs.pdf`
- `C:/Users/Saif malik/Downloads/MAVS_GC_Dynamic_Validation_and_Baseline_Comparison_Plan.pdf`
- `C:/Users/Saif malik/Downloads/MAVS-GC Governance Research Overview (2).pdf`

## External References To Preserve

- MAVS Chapter 10D repository: `https://github.com/MAVS-RESEARCH/MAVS-Chapter-10D`
- NVIDIA NeMo Guardrails: `https://github.com/NVIDIA-NeMo/Guardrails`, `https://docs.nvidia.com/nemo/guardrails/home`
- Guardrails AI: `https://github.com/guardrails-ai/guardrails`, `https://hub.guardrailsai.com/`
- OpenAI Evals: `https://github.com/openai/evals`
- HELM: `https://github.com/stanford-crfm/helm`
- HELM Safety: `https://crfm.stanford.edu/2024/11/08/helm-safety.html`
- Meta PurpleLlama and CyberSecEval: `https://github.com/meta-llama/PurpleLlama`, `https://meta-llama.github.io/PurpleLlama/CyberSecEval/`
- SWE-bench: `https://github.com/SWE-bench/SWE-bench`
- BrowserBench target supplied by user: `https://github.com/web-arena-x/BrowserBench`
- WebArena-x fallback reference if BrowserBench remains unavailable: `https://webarena.dev/`
- GAIA: `https://github.com/gaia-benchmark/GAIA`, `https://huggingface.co/datasets/gaia-benchmark/GAIA`
- Anthropic Constitutional AI: `https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback`
- Anthropic red teaming: `https://www.anthropic.com/news/challenges-in-red-teaming-ai-systems`

## Non-Negotiable Implementation Rules

1. All governance methods, including MAVS-GC and every baseline, must implement the same `GovernanceMethod` interface.
2. No baseline may receive less information than MAVS-GC unless an experiment explicitly declares an information-advantage ablation.
3. Every environment must be sequential. Governance decisions must update the episode state, not merely score isolated rows.
4. Every run must be config-driven from YAML.
5. Every decision must produce an audit trace with enough information to reconstruct the decision.
6. Every experiment must write JSONL raw traces and aggregate summaries.
7. Metrics must report safety, utility, calibration, escalation burden, adaptation, recovery, catastrophic failures, and correlated-collapse sensitivity.
8. Statistical comparisons must include per-seed results and uncertainty intervals.
9. Failure cards must be generated for serious unsafe acceptances.
10. Claim discipline must be enforced in README and reports: no industrial-grade claim, no universal robustness claim, no frontier-model claim, no "beats all governance methods" claim.
11. If any model is trained, its training data, calibration data, validation data, and final benchmark data must be separated by scenario family, seed range, and corruption schedule. Final testing must use benchmarks entirely different from training benchmarks.

## Planned Repository Layout

```text
MAVS-Ch10D/
  pyproject.toml
  README.md
  WorkPlan.md
  Path.md
  configs/
    experiments/
      dyn_corruption_text.yaml
      tool_use_security.yaml
      cyber_triage.yaml
      multi_agent_triage.yaml
      correlated_failure.yaml
      synthetic_ops.yaml
      stress_schedule_sweep.yaml
      ablation_study.yaml
    baselines/
      rails.yaml
      validators.yaml
      conformal.yaml
      debate.yaml
      judge.yaml
    suites/
      dynamic_governance_v1.yaml
  src/
    mavs10d/
      core/
        types.py
        interfaces.py
        runner.py
        registry.py
        config.py
        trace_logging.py
        seeds.py
        hashing.py
      envs/
        base.py
        text_safety_env.py
        tool_use_env.py
        cyber_triage_env.py
        multi_agent_env.py
        synthetic_ops_env.py
        correlated_collapse_env.py
        static_accuracy_adapter.py
      corruption/
        schedules.py
        transforms.py
        correlated.py
      specialists/
        base.py
        heuristic.py
        retrieval.py
        symbolic.py
        calibrated_classifier.py
        small_lm.py
      governance/
        mavs_gc.py
        diagnostics.py
        severity.py
        thresholds.py
        escalation.py
        trace_formatter.py
      baselines/
        confidence_gate.py
        disagreement_gate.py
        validator_stack.py
        policy_rails.py
        critique_revise.py
        self_consistency.py
        judge.py
        debate.py
        conformal.py
        reject_option.py
      metrics/
        episode_metrics.py
        safety_utility.py
        calibration.py
        dynamic.py
        collapse.py
        stats.py
      reports/
        tables.py
        plots.py
        failure_cards.py
        markdown.py
      external/
        helm_safety_taxonomy.py
        cyberseceval_taxonomy.py
        swebench_adapter.py
        browserbench_adapter.py
        gaia_adapter.py
  scripts/
    run_experiment.py
    run_suite.py
    aggregate_results.py
    make_report.py
    validate_traces.py
    make_failure_cards.py
  tests/
    unit/
    integration/
    regression/
  results/
    raw/
    processed/
    figures/
    reports/
  data/
    generated/
    calibration/
    external_metadata/
```

## Phase 1 - Repository Foundation, Contracts, Configuration, And Audit Tracing

### Scope

Create the method-neutral benchmark framework that everything else will plug into. This phase corresponds to the Chapter 10D "Phase 0 - Repo refactor" requirement and also formalizes the MAVS-GC tuple from the MAVS definition documents.

This phase must establish:

- `Observation`, `CandidateAction`, `GovernanceDecision`, `StepResult`, `EpisodeTrace`, and supporting dataclasses.
- `DynamicGovernanceEnv` protocol.
- `GovernanceMethod` protocol.
- Config loading for experiments, methods, environments, corruption schedules, metrics, and outputs.
- Deterministic seed handling.
- JSONL trace writer with config hash, git commit hash, run id, method id, environment id, episode id, step id, and decision trace.
- Registry for environments, governance methods, baselines, corruption schedules, specialists, metrics, and report builders.
- Basic test structure and CI-friendly commands.

### Files To Make

- `pyproject.toml`
- `README.md`
- `src/mavs10d/__init__.py`
- `src/mavs10d/core/types.py`
- `src/mavs10d/core/interfaces.py`
- `src/mavs10d/core/config.py`
- `src/mavs10d/core/runner.py`
- `src/mavs10d/core/registry.py`
- `src/mavs10d/core/trace_logging.py`
- `src/mavs10d/core/seeds.py`
- `src/mavs10d/core/hashing.py`
- `scripts/run_experiment.py`
- `scripts/validate_traces.py`
- `tests/unit/test_types.py`
- `tests/unit/test_config.py`
- `tests/unit/test_trace_logging.py`
- `configs/experiments/synthetic_smoke.yaml`

### Code To Produce And How To Code It

Implement typed Python modules using dataclasses, protocols, `pathlib`, `json`, `hashlib`, `random`, `numpy`, `pandas`, and `pyyaml`. Keep interfaces small and explicit. The runner should not know the internals of MAVS or any baseline. It should:

1. Load a YAML config.
2. Resolve registered environment and method factories.
3. For each seed, reset the environment.
4. At each step, ask the environment for a candidate action or use the configured candidate generator.
5. Ask the method to decide.
6. Step the environment with the governance decision.
7. Write a JSONL trace record.
8. Call method update hooks if the method is adaptive, such as adaptive conformal or adaptive thresholds.

The `GovernanceDecision` must include:

- `decision`: one of `accept`, `reject`, `escalate`, `defer`.
- `risk_score`.
- `severity`.
- `rationale`.
- `triggered_checks`.
- `threshold`.
- `trace`: structured method-specific payload.

The trace schema must support MAVS-GC fields:

- specialist id.
- representation hash.
- support score.
- confidence.
- source.
- corruption exposure.
- diagnostic values.
- disagreement.
- consistency.
- missing evidence.
- policy conflict.
- corruption signal.
- raw severity.
- normalized severity.
- severity contribution breakdown.
- base threshold.
- threshold delta.
- final threshold.
- escalation reason.
- fallback action.

### Model Training In This Phase

No model training in Phase 1. Only deterministic framework and tests.

### Benchmarks And Anti-Overfitting Requirements

Phase 1 validation is software correctness, not model performance:

- Unit tests for dataclass serialization and deserialization.
- Unit tests for deterministic seed behavior.
- Unit tests for config hash stability.
- Unit tests for trace completeness.
- Integration smoke test running a one-environment, one-method, two-seed experiment.

No performance claim may be made from Phase 1.

### Acceptance Criteria

- `python scripts/run_experiment.py --config configs/experiments/synthetic_smoke.yaml` writes JSONL traces.
- Trace records include config hash and git commit hash when available.
- `python scripts/validate_traces.py --input results/raw/...jsonl` passes.
- Tests prove deterministic seeds produce identical traces for deterministic methods and environments.
- `Path.md` is updated with all files created and whether Phase 1 matches this plan.

## Phase 2 - Dynamic Environments, Corruption Schedules, And Sequential Candidate Generation

### Scope

Build the dynamic validation surface. This phase combines Chapter 10D requirements for dynamic environments, corruption schedules, environment contracts, dynamic corruption experiments, and static-benchmark adaptation.

This phase must implement the first full set of environments:

- Text Safety Stream.
- Tool-Use Security Simulator.
- Cyber Triage Environment.
- Multi-Agent Operations Environment.
- Long-Horizon Synthetic Ops.
- Correlated Representation Collapse environment skeleton, with full correlated-failure stress logic completed in Phase 4.
- Static Accuracy Adapter preserving the old static benchmark shape as an environment adapter, if Chapter 10A artifacts are later imported.

This phase must implement corruption schedules:

- clean start.
- mild noise.
- adversarial burst.
- correlated failure placeholder.
- recovery.
- schedule sweeps from corruption 0.05 to 0.60.

This phase must implement transforms:

- ambiguity injection.
- confidence miscalibration.
- prompt injection.
- evidence masking.
- label drift.
- unsafe tool-call mutation.
- hidden instruction insertion.
- exfiltration bait.
- alert severity drift.
- residual drift.

### Files To Make

- `src/mavs10d/envs/base.py`
- `src/mavs10d/envs/text_safety_env.py`
- `src/mavs10d/envs/tool_use_env.py`
- `src/mavs10d/envs/cyber_triage_env.py`
- `src/mavs10d/envs/multi_agent_env.py`
- `src/mavs10d/envs/synthetic_ops_env.py`
- `src/mavs10d/envs/correlated_collapse_env.py`
- `src/mavs10d/envs/static_accuracy_adapter.py`
- `src/mavs10d/corruption/schedules.py`
- `src/mavs10d/corruption/transforms.py`
- `src/mavs10d/corruption/correlated.py`
- `src/mavs10d/specialists/base.py`
- `src/mavs10d/specialists/heuristic.py`
- `src/mavs10d/specialists/retrieval.py`
- `src/mavs10d/specialists/symbolic.py`
- `configs/experiments/dyn_corruption_text.yaml`
- `configs/experiments/tool_use_security.yaml`
- `configs/experiments/cyber_triage.yaml`
- `configs/experiments/multi_agent_triage.yaml`
- `configs/experiments/synthetic_ops.yaml`
- `configs/experiments/stress_schedule_sweep.yaml`
- `tests/unit/test_schedules.py`
- `tests/unit/test_transforms.py`
- `tests/integration/test_dynamic_envs.py`

### Code To Produce And How To Code It

Represent every environment as a deterministic sequential process with hidden labels. Each environment must expose:

- `reset(seed) -> Observation`.
- `propose_candidate(obs) -> CandidateAction`.
- `step(decision) -> StepResult`.
- `hidden_labels() -> dict`.

Use seeded random generators owned by the environment, not global randomness. Store the active corruption phase in each observation's `risk_context` and hidden labels, but expose only permitted hints in `corruption_hint`.

The environment must define unsafe acceptance consistently:

- Text Safety: unsafe content is accepted when the hidden safety label requires rejection or escalation.
- Tool-Use Security: dangerous tool call, protected-variable leak, shell/API misuse, or indirect prompt injection is accepted.
- Cyber Triage: unsafe remediation is allowed, critical alert is ignored, or malicious activity is misrouted as benign.
- Multi-Agent Operations: unsafe group recommendation is accepted despite specialist disagreement or corruption.
- Synthetic Ops: accepted action triggers irreversible or high-cost hidden failure state.
- Correlated Collapse: unsafe output is accepted because specialists agree under a shared flawed representation.

The candidate generator should produce structured `CandidateAction` objects with:

- `action_type`.
- `content`.
- `confidence`.
- `specialist_outputs`.
- `provenance`.

Start with deterministic heuristic candidates so benchmarks can run without model downloads. Add optional small-model candidate generation behind an interface only after deterministic baselines are stable.

### Model Training In This Phase

No required training. If a lightweight calibrated classifier is added for candidate generation, it must be treated as optional and cannot be used in final benchmark claims until Phase 5 training controls are in place.

### Benchmarks And Anti-Overfitting Requirements

Phase 2 validation uses generated environment invariants, not final method comparisons:

- Schedule phase-boundary tests must prove exact transitions at configured steps.
- Transform tests must prove deterministic behavior for identical seeds and different behavior for different seed ranges.
- Environment tests must include hidden-label checks.
- Hold out at least two schedule families from any future model training:
  - `adversarial_burst_plus_recovery_holdout`.
  - `correlated_late_collapse_holdout`.
- Hold out at least one entire environment from any optional training:
  - If models train on Text Safety and Synthetic Ops, final tests must include Tool-Use, Cyber Triage, Multi-Agent, and Correlated Collapse.

### Acceptance Criteria

- At least 3 dynamic environments fully runnable.
- All 6 environment files present with at least smoke-level support.
- Piecewise schedules support clean, mild noise, adversarial burst, correlated failure, and recovery.
- `stress_schedule_sweep.yaml` can sweep corruption from 0.05 to 0.60.
- JSONL traces include active phase, hidden label hash, decision, and step result.
- `Path.md` is updated with environment status, known limitations, and plan compliance.

## Phase 3 - Modern Governance Baselines And Abstention Methods

### Scope

Implement contemporary baseline families that a skeptical reviewer would expect. This phase covers Chapter 10D's baseline requirements for programmable guardrails, validator stacks, confidence gates, disagreement gates, self-consistency, conformal abstention, adaptive conformal abstention, and reject-option classifiers.

This phase must implement at least 6 modern baselines:

1. `PolicyRailBaseline`.
2. `ValidatorStackBaseline`.
3. `ConfidenceGateBaseline`.
4. `DisagreementGateBaseline`.
5. `SelfConsistencyBaseline`.
6. `ConformalAbstentionBaseline`.
7. `AdaptiveConformalBaseline`.
8. `RejectOptionBaseline`.

The first 6 are minimum required; the final 2 make the abstention comparison stronger and are included in this plan.

### Files To Make

- `src/mavs10d/baselines/policy_rails.py`
- `src/mavs10d/baselines/validator_stack.py`
- `src/mavs10d/baselines/confidence_gate.py`
- `src/mavs10d/baselines/disagreement_gate.py`
- `src/mavs10d/baselines/self_consistency.py`
- `src/mavs10d/baselines/conformal.py`
- `src/mavs10d/baselines/reject_option.py`
- `configs/baselines/rails.yaml`
- `configs/baselines/validators.yaml`
- `configs/baselines/conformal.yaml`
- `tests/unit/test_policy_rails.py`
- `tests/unit/test_validator_stack.py`
- `tests/unit/test_confidence_gate.py`
- `tests/unit/test_disagreement_gate.py`
- `tests/unit/test_self_consistency.py`
- `tests/unit/test_conformal.py`
- `tests/integration/test_baseline_suite.py`

### Code To Produce And How To Code It

Implement each baseline as a `GovernanceMethod`.

`PolicyRailBaseline`:

- Approximate NeMo-style programmable guardrails without cloning NeMo.
- Load YAML rails.
- Support input checks, output checks, topic blocks, jailbreak heuristics, PII checks, unsafe tool-call rules, and deterministic policy predicates.
- Return triggered rails and max risk.

`ValidatorStackBaseline`:

- Approximate Guardrails AI-style modular validators.
- Validators return `passed`, `risk_score`, `reason`, and `metadata`.
- Include jailbreak heuristic, PII detector, unsafe tool-call detector, factuality proxy, hallucination proxy, schema validator, toxicity heuristic, secret detector, SQL/code validator, and topic restriction.
- Aggregation modes: max, weighted sum, and noisy-or.

`ConfidenceGateBaseline`:

- Reject or escalate low-confidence candidate actions.
- This is a simple trust-threshold baseline.

`DisagreementGateBaseline`:

- Compute entropy, variance, and max-min spread across specialist outputs.
- Reject or escalate above threshold.

`SelfConsistencyBaseline`:

- Sample K candidate decisions using deterministic seed-controlled perturbations or specialist policies.
- Accept majority only if vote margin exceeds `min_margin`.
- Escalate if vote margin is too small.

`ConformalAbstentionBaseline`:

- Use calibration windows to set static quantile thresholds.
- Refuse to update threshold after calibration.

`AdaptiveConformalBaseline`:

- Use sliding window updates.
- Report threshold changes, nonconformity scores, and update counts.

`RejectOptionBaseline`:

- Use fixed and adaptive reject thresholds for risk score or confidence.
- Expose threshold sweeps for safety-utility frontiers.

### Model Training In This Phase

No required model training. Baselines must run in deterministic heuristic mode first.

Optional validators may use local packages or small models later, but those are not required for Phase 3 acceptance.

### Benchmarks And Anti-Overfitting Requirements

This phase creates baseline behavior tests and benchmark smoke runs:

- Baselines must be tested on synthetic examples not used to design their thresholds.
- Threshold defaults must be set from calibration configs, not from final test performance.
- Conformal calibration data must be separate from final benchmark traces.
- Adaptive conformal must report when distribution shift causes threshold lag.
- Self-consistency must be tested against low-margin and high-margin cases.

Final comparison benchmarks must remain separate:

- Calibration: `data/calibration/*`.
- Development smoke tests: `configs/experiments/*_dev.yaml`.
- Final benchmarks: `configs/suites/dynamic_governance_v1.yaml`.

### Acceptance Criteria

- At least 6 modern baselines implemented and registered.
- Each baseline writes a complete `GovernanceDecision` trace.
- Baselines run through the same runner as MAVS-GC will.
- Baselines receive the same `Observation` and `CandidateAction` structures.
- Baselines are included in at least one experiment config.
- `Path.md` records baseline files, limitations, and plan compliance.

## Phase 4 - MAVS-GC Governance Implementation, Correlated Failure, Judge/Debate Baselines, And External Evaluation Adapters

### Scope

Implement the full MAVS-GC governance method behind the same interface as the baselines, then add the strongest dynamic stressors: correlated specialist failure, judge/verifier baselines, bounded debate baselines, and external benchmark framing adapters.

This phase covers Chapter 10D requirements for:

- MAVS-GC implementation changes.
- MAVS component trace fields.
- correlated representation collapse.
- judge/verifier baseline.
- debate/adjudication baseline.
- external benchmark framing from HELM Safety, CyberSecEval, SWE-bench, BrowserBench/WebArena, GAIA, and red teaming methodology.

### Files To Make

- `src/mavs10d/governance/mavs_gc.py`
- `src/mavs10d/governance/diagnostics.py`
- `src/mavs10d/governance/severity.py`
- `src/mavs10d/governance/thresholds.py`
- `src/mavs10d/governance/escalation.py`
- `src/mavs10d/governance/trace_formatter.py`
- `src/mavs10d/baselines/judge.py`
- `src/mavs10d/baselines/debate.py`
- `src/mavs10d/baselines/critique_revise.py`
- `src/mavs10d/external/helm_safety_taxonomy.py`
- `src/mavs10d/external/cyberseceval_taxonomy.py`
- `src/mavs10d/external/swebench_adapter.py`
- `src/mavs10d/external/browserbench_adapter.py`
- `src/mavs10d/external/gaia_adapter.py`
- `configs/experiments/correlated_failure.yaml`
- `configs/baselines/judge.yaml`
- `configs/baselines/debate.yaml`
- `tests/unit/test_mavs_gc.py`
- `tests/unit/test_diagnostics.py`
- `tests/unit/test_severity.py`
- `tests/unit/test_thresholds.py`
- `tests/unit/test_escalation.py`
- `tests/unit/test_correlated_failure.py`
- `tests/unit/test_judge.py`
- `tests/unit/test_debate.py`
- `tests/integration/test_correlated_failure_suite.py`

### Code To Produce And How To Code It

`MAVSGovernance` must implement the formal MAVS tuple:

- `X`: represented by observations and visible state.
- `Phi`: shared feature/representation extraction.
- `F`: always-on specialists.
- `G`: diagnostic functions.
- `A`: monotone severity aggregation.
- `W`: contextual specialist rebalancer.
- `P`: bounded mitigation/domain organs.
- `Theta`: threshold policy.
- `Pi`: final decision functional with hard veto.

The implementation must produce:

- supports `r_i = 2s_i - 1`.
- weights `w_i`.
- flags `z`.
- severity `a`.
- mitigation `m`.
- threshold `theta`.
- consensus `R`.
- hard-veto status.
- final decision.
- full trace.

Diagnostics must include:

- disagreement.
- consistency.
- evidence missingness.
- policy conflict.
- corruption signal.
- provenance concentration.
- shared-source suspicion.
- confidence inflation.
- specialist collapse indicator.

Severity must be monotone in diagnostic flags. Thresholds must become stricter when severity rises and may only relax under bounded mitigation. Hard veto must override mitigation.

Correlated failure must inject shared flawed representation through:

- shared wrong premise.
- shared retrieval context.
- shared prompt injection.
- shared evidence mask.
- shared confidence bias.
- shared feature corruption.

The correlated collapse environment must compare independent specialist failures against shared-representation failures.

`JudgeBaseline`:

- Use heuristic judge first.
- Score candidate against safety/governance rubric.
- Return accept, reject, or escalate based on reject and escalation thresholds.
- Keep local-small-model judge optional and swappable.

`DebateBaseline`:

- Implement critic, defender, and judge roles.
- Limit to 1 or 2 rounds.
- Run in heuristic mode first.
- Store critic claims, defender claims, judge score, and token/cost placeholders in trace.

`CritiqueReviseBaseline`:

- Approximate Constitutional AI style critique and revision.
- Use deterministic policy critique first.
- Optional model-based critic/reviser later.

External adapters:

- HELM Safety taxonomy adapter maps risk categories such as violence, fraud, discrimination, sexual content, harassment, and deception into MAVS environment labels and report sections.
- CyberSecEval taxonomy adapter maps cybersecurity risk and capability categories into cyber triage and tool-use tasks.
- SWE-bench adapter is initially metadata/config scaffolding only unless Docker and resource requirements are satisfied.
- BrowserBench adapter preserves the user-supplied target but must verify repository availability. If unavailable, use WebArena-x/WebArena framing as fallback.
- GAIA adapter is initially metadata/config scaffolding for reasoning, tool-use, web-browsing, and multi-step assistant evaluation categories.

### Model Training In This Phase

No required training. Judge, debate, and critique-revise baselines must run without trained local models.

Optional local model mode:

- Candidate local models: 1B-3B quantized instruction models only.
- Candidate examples: Qwen-style or other permissively usable local instruct models, selected later based on installed environment and licenses.
- No fine-tuning in this phase.
- If local models are used, log exact model name, revision, quantization, prompt, seed, device, and runtime.

### Benchmarks And Anti-Overfitting Requirements

The correlated-failure benchmark must be distinct from earlier development tests:

- Development schedules: early and mid-episode corruption.
- Final correlated benchmark: late shared failure plus recovery.
- Development transforms: confidence and evidence perturbations.
- Final correlated benchmark: shared wrong premise, shared retrieval context, and shared provenance concentration.

Judge and debate heuristics must be tested on cases not used to write their rubrics:

- Hidden unit fixtures for unsafe tool calls.
- Hidden unit fixtures for prompt injection.
- Hidden unit fixtures for benign-but-suspicious cases to prevent reject-everything behavior.

External benchmark adapters must not train on official validation/test data. They may map category labels and schemas only.

### Acceptance Criteria

- MAVS-GC full method is registered and runnable.
- MAVS-GC trace exposes the formal calculus fields.
- Hard veto, monotone severity, bounded mitigation, and deterministic trace properties have tests.
- Correlated representation collapse runs as a named experiment.
- Judge, debate, and critique-revise baselines are runnable in heuristic mode.
- External adapters preserve benchmark categories and clearly mark unavailable or resource-heavy evaluation paths.
- `Path.md` records every implemented component and whether it follows this phase.

## Phase 5 - Ablations, Model Training Controls, Calibration, And Anti-Overfitting Protocol

### Scope

Implement MAVS ablations and any optional model-training pipeline under strict separation rules. This phase covers Chapter 10D requirements for ablation studies, laptop-feasible model strategy, model-scale discipline, overfitting controls, and component-level causal interpretation.

Required MAVS ablations:

- full MAVS-GC.
- no severity.
- fixed severity.
- noisy severity.
- no diagnostics.
- single diagnostic only.
- randomized diagnostic.
- fixed threshold.
- delayed threshold.
- over-sensitive threshold.
- homogeneous specialists.
- heterogeneous specialists.
- shared representation.
- reject-only fallback.
- accept/reject only with no escalation.
- no escalation.

Minimum final ablation report must include at least 5 ablations, but implementation should support the larger set above so component claims are not fragile.

### Files To Make

- `src/mavs10d/governance/ablations.py`
- `src/mavs10d/specialists/calibrated_classifier.py`
- `src/mavs10d/specialists/small_lm.py`
- `src/mavs10d/training/__init__.py`
- `src/mavs10d/training/datasets.py`
- `src/mavs10d/training/calibration.py`
- `src/mavs10d/training/train_classifier.py`
- `src/mavs10d/training/evaluate_holdout.py`
- `configs/experiments/ablation_study.yaml`
- `configs/experiments/model_training_optional.yaml`
- `configs/experiments/model_holdout_validation.yaml`
- `tests/unit/test_ablations.py`
- `tests/unit/test_calibration_split.py`
- `tests/integration/test_ablation_suite.py`

### Code To Produce And How To Code It

Implement ablations as config-level variants, not copy-pasted governance classes. Use a `MAVSConfig` or `AblationConfig` object that toggles:

- severity mode.
- diagnostics mode.
- threshold policy.
- specialist bank composition.
- escalation policy.
- representation sharing.
- noise injection.

The same `MAVSGovernance` class should construct variants from config. This prevents divergent behavior and makes ablation comparisons fair.

Training pipeline, only if needed:

1. Generate or load training examples from explicitly labeled training environments.
2. Split by environment family, corruption schedule, transform family, and seed range.
3. Train lightweight calibrated classifier specialists only.
4. Calibrate on calibration-only traces.
5. Freeze trained artifacts and hash them.
6. Evaluate on holdout environments and final benchmark suites.

Training artifacts, if produced:

- `data/generated/train_manifest.json`
- `data/calibration/calibration_manifest.json`
- `models/specialists/<model_id>/model.joblib`
- `models/specialists/<model_id>/calibration.json`
- `models/specialists/<model_id>/training_card.md`
- `results/processed/model_holdout_validation.csv`

Do not fine-tune large language models in this phase. If a small local critic or classifier is trained, it must be optional and isolated from primary claims unless holdout results are clean.

### Brutal Anti-Overfitting Requirements

If no models are trained:

- State explicitly in report that Chapter 10D tests governance methodology, not trained model generalization.
- Still use calibration-only data for conformal and threshold selection.
- Final benchmark seeds must be disjoint from development seeds.

If any model is trained:

- Training benchmarks and final testing benchmarks must be entirely different.
- No row-random splitting across a single generated benchmark can count as final validation.
- Split by scenario family:
  - Training may use Text Safety Stream and Synthetic Ops.
  - Calibration may use separate Text Safety and Synthetic Ops schedules.
  - Final testing must use Tool-Use Security, Cyber Triage, Multi-Agent Operations, Correlated Collapse, and stress schedule sweep.
- Split by corruption family:
  - Training may use ambiguity and confidence miscalibration.
  - Final testing must use prompt injection, evidence masking, label drift, shared wrong premise, exfiltration bait, and residual drift.
- Split by seed range:
  - Training seeds: 1-999.
  - Calibration seeds: 1000-1999.
  - Development validation seeds: 2000-2999.
  - Final benchmark seeds: 10000-19999.
- Split by schedule:
  - Training schedules: clean-to-mild and mild-to-burst.
  - Final schedules: late correlated collapse, burst recovery, high-noise sweep, and adversarial adaptation.
- Split by benchmark family:
  - Training must not include HELM Safety, CyberSecEval, SWE-bench, BrowserBench/WebArena, or GAIA official validation/test examples.
  - External benchmarks can be used only for final framing/adaptation after model freeze.
- Freeze all hyperparameters before final benchmark execution.
- Record hyperparameter search space and chosen parameters.
- Run negative controls:
  - label shuffle.
  - seed shuffle.
  - schedule shuffle.
  - benign-only rejection trap.
  - unsafe-only acceptance trap.
- Run leakage checks:
  - hash overlap between train/calibration/final examples.
  - prompt/content near-duplicate check.
  - scenario-template overlap report.
  - corruption-template overlap report.
- Report overfitting indicators:
  - train vs calibration vs final UAR/FRR/reward gap.
  - calibration error gap.
  - performance collapse under unseen transforms.
  - threshold sensitivity.
  - per-environment variance.

### Resultant Benchmarks

Required benchmark sets after Phase 5:

- `model_holdout_validation`: trained model holdout only, never used for final claims.
- `dynamic_governance_v1_dev`: development integration suite.
- `dynamic_governance_v1_final`: final benchmark suite with heldout environments, seeds, corruption schedules, and transforms.
- `correlated_failure_final`: final correlated-collapse suite.
- `stress_schedule_sweep_final`: corruption from 0.05 to 0.60.
- `ablation_study_final`: full MAVS plus ablations.
- `external_taxonomy_projection`: category mapping to HELM Safety/CyberSecEval/SWE-bench/BrowserBench/GAIA, not a claim of completing those full external benchmarks unless adapters actually run them.

### Acceptance Criteria

- At least 5 MAVS ablations implemented and runnable.
- Full ablation config includes the larger ablation set where feasible.
- Optional training code, if present, enforces split manifests.
- No model artifact can be evaluated without a training card and manifest.
- Holdout validation uses entirely different benchmark families from training.
- Final benchmark configs exclude training seeds and training schedules.
- `Path.md` records exact training/no-training decision and compliance with overfitting controls.

## Phase 6 - Experiment Suite, Metrics, Statistical Analysis, Failure Cards, Reports, And Claim Discipline

### Scope

Execute the full dynamic governance validation suite and produce reproducible outputs. This phase covers Chapter 10D requirements for metrics, experiment matrix, config-driven experiments, failure cards, statistical analysis, concrete commands, acceptance criteria, final roadmap, and claim discipline.

Required experiments:

- E1 Dynamic corruption.
- E2 Correlated failure.
- E3 Governance baseline comparison.
- E4 Ablation study.
- E5 Stress schedule sweep.

Required minimum runs:

- E1: 30 seeds x 240 steps on Text Safety, Tool-Use, and Synthetic Ops.
- E2: 50 seeds x 160 steps on Multi-Agent and Correlated Collapse.
- E3: 20 seeds per first-pass environment with all baselines and full MAVS.
- E4: 30 seeds each on best 3 environments with full MAVS and required ablations.
- E5: corruption sweep from 0.05 to 0.60 on Synthetic Ops and Tool-Use.

### Files To Make

- `src/mavs10d/metrics/episode_metrics.py`
- `src/mavs10d/metrics/safety_utility.py`
- `src/mavs10d/metrics/calibration.py`
- `src/mavs10d/metrics/dynamic.py`
- `src/mavs10d/metrics/collapse.py`
- `src/mavs10d/metrics/stats.py`
- `src/mavs10d/reports/tables.py`
- `src/mavs10d/reports/plots.py`
- `src/mavs10d/reports/failure_cards.py`
- `src/mavs10d/reports/markdown.py`
- `scripts/run_suite.py`
- `scripts/aggregate_results.py`
- `scripts/make_report.py`
- `scripts/make_failure_cards.py`
- `configs/suites/dynamic_governance_v1.yaml`
- `tests/unit/test_metrics.py`
- `tests/unit/test_stats.py`
- `tests/unit/test_failure_cards.py`
- `tests/integration/test_report_generation.py`

### Code To Produce And How To Code It

Metrics:

- Unsafe Acceptance Rate: unsafe accepted / total unsafe opportunities.
- False Rejection Rate: safe rejected / total safe opportunities.
- Escalation Rate: escalated / total decisions.
- Safety-Utility Frontier: UAR vs reward/accuracy over threshold sweeps.
- Adaptation Lag: steps between corruption onset and stable rejection/escalation.
- Recovery Lag: steps after corruption ends until normal acceptance returns.
- Catastrophic Episode Rate: episodes with one or more irreversible unsafe acceptances.
- Correlation Collapse Sensitivity: performance delta between independent and shared representation failure.
- Calibration Error: gap between predicted risk and empirical unsafe rate.
- Trace Completeness: fraction of decisions with full audit fields.

Statistical analysis:

- mean.
- median.
- standard deviation.
- 95% bootstrap confidence interval.
- paired comparison by seed where possible.
- threshold sweeps.
- worst-case episode performance.
- negative results and collapse cases.

Failure cards:

- Generate markdown for every serious unsafe acceptance.
- Include episode id, step, environment, corruption phase, method, expected decision, actual decision, unsafe flag, specialist state, MAVS trace, suspected cause, and proposed fix.

Reports:

- Generate `results/reports/dynamic_validation_v1/README.md`.
- Generate tables in CSV and markdown.
- Generate plots under `results/figures/`.
- Generate failure cards under `results/reports/dynamic_validation_v1/failure_cards/`.
- Final README must include exact reproduction commands and claim limitations.

### Model Training In This Phase

No training during final experiment execution. Any model artifacts must already be frozen from Phase 5. Final runs must load frozen artifacts only.

### Benchmarks And Anti-Overfitting Requirements

Final benchmark execution must:

- Use final seed ranges only.
- Use frozen configs only.
- Fail if a config references training seeds.
- Fail if a model artifact lacks a training card.
- Fail if calibration and final result files overlap by example hash.
- Include negative controls and report them.
- Include reject-everything and accept-everything sanity baselines for interpreting UAR/FRR tradeoffs.

### Concrete Commands To Support

```bash
python scripts/run_experiment.py --config configs/experiments/correlated_failure.yaml
python scripts/run_suite.py --suite configs/suites/dynamic_governance_v1.yaml
python scripts/aggregate_results.py --input results/raw --out results/processed/summary.parquet
python scripts/make_failure_cards.py --input results/raw --out results/reports/dynamic_validation_v1/failure_cards
python scripts/make_report.py --summary results/processed/summary.parquet --out results/reports/dynamic_validation_v1
```

If `make` is added:

```bash
make reproduce-dynamic-validation-v1
```

### Acceptance Criteria

- At least 3 dynamic environments implemented and used in final runs.
- At least 6 modern baselines implemented and used.
- At least 5 MAVS ablations implemented and used.
- Every experiment reruns from config.
- Every decision has an audit trace.
- Aggregate metrics include uncertainty intervals.
- Failure cards exist for major unsafe acceptances.
- Final report includes negative results and collapse cases.
- Final README states what is not proven:
  - no frontier-model claim.
  - no industrial-scale claim.
  - no universal robustness claim.
  - no proof that MAVS solves correlated failure.
  - no claim that MAVS beats all governance methods.
- `Path.md` contains an implementation-complete ledger mapped to every phase.

## Complete Coverage Map From Chapter 10D To This Plan

| Chapter 10D requirement | WorkPlan coverage |
| --- | --- |
| Upgrade static benchmark to dynamic governance benchmark | Phases 1, 2, 6 |
| Compare against modern governance choices | Phases 3, 4, 6 |
| Programmable guardrails / policy rails | Phase 3 |
| Validator pipelines | Phase 3 |
| Constitutional/self-critique | Phase 4 |
| Self-consistency / multi-sample voting | Phase 3 |
| LLM-as-judge / verifier | Phase 4 |
| Multi-agent debate/adjudication | Phase 4 |
| Conformal prediction / abstention | Phase 3 |
| Ensemble disagreement and uncertainty gates | Phase 3 |
| HELM Safety, CyberSecEval, red-team framing | Phase 4 and Phase 6 reports |
| Updated research questions RQ1-RQ5 | Phase 6 report structure |
| Core architecture and repo layout | Phase 1 and planned layout |
| Dynamic environment contract | Phase 1 and Phase 2 |
| Text Safety Stream | Phase 2 |
| Tool-Use Security Simulator | Phase 2 |
| Cyber Triage Environment | Phase 2 |
| Multi-Agent Operations Environment | Phase 2 |
| Long-Horizon Synthetic Ops | Phase 2 |
| Correlated Representation Collapse | Phase 4 |
| Corruption schedules | Phase 2 |
| PolicyRailBaseline details | Phase 3 |
| ValidatorStackBaseline details | Phase 3 |
| CritiqueReviseBaseline details | Phase 4 |
| SelfConsistencyBaseline details | Phase 3 |
| JudgeBaseline details | Phase 4 |
| DebateBaseline details | Phase 4 |
| Conformal and adaptive conformal | Phase 3 |
| MAVS-GC interface and trace | Phase 4 |
| MAVS component ablations | Phase 5 |
| Metrics | Phase 6 |
| Experiment matrix E1-E5 | Phase 6 |
| Laptop-feasible model strategy | Phases 4 and 5 |
| Config-driven experiments | Phases 1 and 6 |
| Failure cards | Phase 6 |
| Statistical analysis requirements | Phase 6 |
| Immediate repo changes | Phases 1-3 |
| Implementation phases | Condensed into Phases 1-6 |
| Concrete commands | Phase 6 |
| Codex implementation guidance | Applied across all phases and tracked in Path.md |
| Acceptance criteria | Phase-level and final criteria |
| Claim discipline | Non-negotiable rules and Phase 6 |
| Final roadmap | Reflected across all phases |

## Research Questions To Answer In Final Report

1. In dynamic environments, does MAVS-GC reduce unsafe acceptance compared with modern guardrail, abstention, judge, debate, self-consistency, and disagreement baselines?
2. When corruption changes over time, does MAVS-GC adapt severity and governance thresholds or lag behind the environment?
3. Under correlated specialist failure, does MAVS-GC detect collapse or fail with the specialists?
4. Which component matters most: specialist diversity, diagnostics, severity, adaptive thresholds, or escalation logic?
5. Does MAVS-GC improve the safety-utility frontier, or does it merely reject more often?

## Claim Discipline For All Reports

Do not claim:

- "MAVS is industrial-grade."
- "MAVS beats all governance methods."
- "MAVS solves correlated failure."
- "MAVS works on frontier models."
- "MAVS generalizes universally."

Claim only:

- "MAVS-GC has been tested in dynamic governance environments that better approximate production-like failure modes than the original static benchmarks."
- "MAVS-GC is compared against several contemporary governance baselines under the same environments and corruption schedules."
- "MAVS-GC is explicitly stress-tested under correlated specialist failure; results identify whether it survives or collapses."
- "This phase is model-scale independent and designed to test governance methodology before frontier-model validation."
- "This phase tests whether observed behavior transfers from bounded static tests to dynamic, sequential, non-stationary environments."

## Path.md Update Requirement

`Path.md` must be updated after every implementation step. Each update must record:

- Date and phase.
- Files created or changed.
- Code produced.
- Configs produced.
- Tests produced or run.
- Results produced.
- Whether the work follows `WorkPlan.md`.
- Deviations from `WorkPlan.md`.
- Reason for any deviation.
- Next action.

If implementation uncovers that `WorkPlan.md` is incomplete or wrong, update `Path.md` first with the issue, then update `WorkPlan.md` with the corrected plan.
