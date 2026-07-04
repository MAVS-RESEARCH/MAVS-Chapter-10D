from __future__ import annotations

from pathlib import Path

import pandas as pd

from mavs10d.core.trace_logging import console_log

CLAIM_LIMITATIONS = (
    "No frontier-model claim.",
    "No industrial-scale claim.",
    "No universal robustness claim.",
    "No proof that MAVS solves correlated failure.",
    "No claim that MAVS beats all governance methods.",
)


def read_summary(path: str | Path) -> pd.DataFrame:
    # console.log: phase6.reports.markdown.read_summary.start
    console_log("phase6.reports.markdown.read_summary.start", path=str(path))
    summary_path = Path(path)
    if summary_path.suffix == ".parquet":
        frame = pd.read_parquet(summary_path)
    else:
        frame = pd.read_csv(summary_path)
    # console.log: phase6.reports.markdown.read_summary.complete
    console_log("phase6.reports.markdown.read_summary.complete", rows=len(frame))
    return frame


def write_final_readme(
    summary: pd.DataFrame,
    out_dir: str | Path,
    *,
    table_paths: dict[str, Path],
    figure_paths: list[Path],
    failure_card_count: int,
) -> Path:
    # console.log: phase6.reports.markdown.write.start
    console_log("phase6.reports.markdown.write.start", rows=len(summary), out_dir=str(out_dir))
    root = Path(out_dir)
    root.mkdir(parents=True, exist_ok=True)
    readme = root / "README.md"
    negative_results = _negative_results(summary)
    collapse_cases = _collapse_cases(summary)
    text = "\n".join(
        [
            "# MAVS Chapter 10D Dynamic Validation V1",
            "",
            "## Reproduction Commands",
            "",
            "```bash",
            "python scripts/run_experiment.py --config configs/experiments/correlated_failure.yaml",
            "python scripts/run_suite.py --suite configs/suites/dynamic_governance_v1.yaml",
            "python scripts/aggregate_results.py --input results/raw --out results/processed/summary.parquet",
            "python scripts/make_failure_cards.py --input results/raw --out results/reports/dynamic_validation_v1/failure_cards",
            "python scripts/make_report.py --summary results/processed/summary.parquet --out results/reports/dynamic_validation_v1",
            "```",
            "",
            "## Scope",
            "",
            "This report evaluates dynamic governance behavior from reproducible MAVS Chapter 10D traces. No training is performed during final execution; any trained model path must load already frozen Phase 5 artifacts only.",
            "",
            "## Produced Artifacts",
            "",
            f"- Summary CSV: `{table_paths.get('summary_csv')}`",
            f"- Summary Markdown: `{table_paths.get('summary_md')}`",
            f"- Figures: `{', '.join(str(path) for path in figure_paths)}`",
            f"- Failure card count: `{failure_card_count}`",
            "",
            "## Negative Results And Collapse Cases",
            "",
            negative_results,
            "",
            collapse_cases,
            "",
            "## Claim Limitations",
            "",
            *[f"- {item}" for item in CLAIM_LIMITATIONS],
            "",
        ]
    )
    readme.write_text(text, encoding="utf-8")
    # console.log: phase6.reports.markdown.write.complete
    console_log("phase6.reports.markdown.write.complete", path=str(readme))
    return readme


def _negative_results(summary: pd.DataFrame) -> str:
    if summary.empty or "unsafe_acceptance_rate" not in summary:
        return "- No summary rows were available."
    negative = summary[summary["unsafe_acceptance_rate"] > 0.0]
    if negative.empty:
        return "- No unsafe-acceptance negative result appears in the aggregated summary."
    rows = [
        f"- `{row.method_id}` on `{row.environment_family}` has UAR `{row.unsafe_acceptance_rate:.4f}`."
        for row in negative.itertuples()
    ]
    return "\n".join(rows)


def _collapse_cases(summary: pd.DataFrame) -> str:
    if summary.empty or "correlation_collapse_sensitivity" not in summary:
        return "- Correlated-collapse sensitivity was not available."
    collapse = summary[summary["correlation_collapse_sensitivity"] > 0.0]
    if collapse.empty:
        return "- No positive correlated-collapse sensitivity was observed in the aggregate rows."
    rows = [
        f"- `{row.method_id}` sensitivity `{row.correlation_collapse_sensitivity:.4f}` in `{row.environment_family}`."
        for row in collapse.itertuples()
    ]
    return "\n".join(rows)
