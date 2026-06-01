"""
Simple experiment logging utilities.

This module helps researchers keep lightweight records of experiments,
assumptions, parameters, and results.
"""

import csv
from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path


@dataclass
class ExperimentLog:
    """
    A simple record for one experiment run.
    """

    name: str
    description: str
    dataset: str
    parameters: str
    result_summary: str
    notes: str = ""
    created_at: str = ""

    def __post_init__(self) -> None:
        if not self.created_at:
            self.created_at = datetime.now().isoformat(timespec="seconds")


def save_experiment_log(log: ExperimentLog, file_path: str | Path) -> Path:
    """
    Append one experiment log to a CSV file.

    Parameters
    ----------
    log:
        ExperimentLog instance.
    file_path:
        Target CSV file path.

    Returns
    -------
    Path
        Path to the saved CSV file.
    """
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    row = asdict(log)
    file_exists = path.exists()

    with path.open("a", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=row.keys())

        if not file_exists:
            writer.writeheader()

        writer.writerow(row)

    return path


def create_example_log() -> ExperimentLog:
    """
    Create an example experiment log.
    """
    return ExperimentLog(
        name="example_experiment",
        description="A placeholder experiment for demonstrating the log format.",
        dataset="sample_dataset",
        parameters="window=20, metric=mean",
        result_summary="No real result. This is only an example.",
        notes="Replace this example with your own experiment details.",
    )


if __name__ == "__main__":
    example = create_example_log()
    saved_path = save_experiment_log(example, "logs/experiment_log.csv")
    print(f"Experiment log saved to: {saved_path}")
