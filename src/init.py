"""Quant Investor research toolkit."""

__version__ = "0.1.0"

from .checklist import build_checklist_markdown, save_checklist
from .config import describe_project_structure, ensure_project_folders
from .experiment_log import ExperimentLog, create_example_log, save_experiment_log

__all__ = [
    "__version__",
    "build_checklist_markdown",
    "save_checklist",
    "describe_project_structure",
    "ensure_project_folders",
    "ExperimentLog",
    "create_example_log",
    "save_experiment_log",
]
