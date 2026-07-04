from mavs10d.baselines.policy_rails import PolicyRailBaseline
from mavs10d.core.config import MethodConfig
from mavs10d.core.types import trace_supports_mavs_fields

from tests.unit.baseline_test_utils import make_candidate, make_observation


def test_policy_rails_load_yaml_and_reject_unsafe_tool() -> None:
    baseline = PolicyRailBaseline(
        MethodConfig(
            id="rails_test",
            type="policy_rails",
            params={"rails_path": "configs/baselines/rails.yaml", "threshold": 0.55},
        )
    )
    baseline.reset(1)
    obs = make_observation()
    candidate = make_candidate(action_type="tool_call", content="call shell_exec", risk_proxy=0.20)

    decision = baseline.decide(obs, candidate)

    assert decision.decision == "reject"
    assert "unsafe_tool_rail" in decision.triggered_checks
    assert trace_supports_mavs_fields(decision.trace)


def test_policy_rails_accept_benign_candidate() -> None:
    baseline = PolicyRailBaseline(
        MethodConfig(
            id="rails_test",
            type="policy_rails",
            params={"rails_path": "configs/baselines/rails.yaml", "threshold": 0.55},
        )
    )
    obs = make_observation()
    candidate = make_candidate(risk_proxy=0.10)

    decision = baseline.decide(obs, candidate)

    assert decision.decision == "accept"
    assert decision.triggered_checks == []

