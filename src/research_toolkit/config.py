"""
Project configuration helpers.

This module provides small utilities for creating and managing a simple
research project directory structure.
"""

from pathlib import Path


DEFAULT_FOLDERS = [
    "data",
    "notebooks",
    "outputs",
    "docs",
    "logs",
]


def get_project_root() -> Path:
    """
    Return the current working directory as the project root.

    This is intentionally simple so the template can be reused across many
    different research projects without requiring extra setup.
    """
    return Path.cwd()


def ensure_project_folders(root: Path | None = None) -> list[Path]:
    """
    Create a basic set of project folders if they do not already exist.

    Parameters
    ----------
    root:
        Optional project root directory. If not provided, the current working
        directory is used.

    Returns
    -------
    list[Path]
        List of created or existing folder paths.
    """
    project_root = root or get_project_root()
    created_folders = []

    for folder_name in DEFAULT_FOLDERS:
        folder_path = project_root / folder_name
        folder_path.mkdir(parents=True, exist_ok=True)
        created_folders.append(folder_path)

    return created_folders


def describe_project_structure(root: Path | None = None) -> dict[str, str]:
    """
    Return a simple description of the expected project folders.

    Parameters
    ----------
    root:
        Optional project root directory. If not provided, the current working
        directory is used.

    Returns
    -------
    dict[str, str]
        Dictionary describing the project structure.
    """
    project_root = root or get_project_root()

    return {
        "root": str(project_root),
        "data": "Raw or processed datasets",
        "notebooks": "Exploratory analysis notebooks",
        "outputs": "Generated figures, tables, and results",
        "docs": "Project documentation",
        "logs": "Experiment logs and workflow notes",
    }


if __name__ == "__main__":
    folders = ensure_project_folders()

    print("Project folders are ready:")
    for folder in folders:
        print(f"- {folder}")
