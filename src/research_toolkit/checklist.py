"""
Reproducibility checklist generator.

This module creates a simple checklist that can be used before sharing or
publishing a research project.
"""

from pathlib import Path


DEFAULT_CHECKLIST_ITEMS = [
    "Research question is clearly defined",
    "Data source is documented",
    "Data collection date is recorded",
    "Preprocessing steps are described",
    "Environment setup is documented",
    "Main scripts or notebooks are organized",
    "Outputs are saved in a dedicated folder",
    "Key assumptions are listed",
    "Limitations are documented",
    "Results can be reproduced from the available files",
]


def build_checklist_markdown(title: str = "Reproducibility Checklist") -> str:
    """
    Build a markdown checklist.

    Parameters
    ----------
    title:
        Title of the checklist document.

    Returns
    -------
    str
        Markdown-formatted checklist.
    """
    lines = [f"# {title}", ""]

    for item in DEFAULT_CHECKLIST_ITEMS:
        lines.append(f"- [ ] {item}")

    lines.append("")
    lines.append("## Notes")
    lines.append("")
    lines.append("Add any project-specific notes here.")

    return "\n".join(lines)


def save_checklist(file_path: str | Path = "docs/reproducibility_checklist.md") -> Path:
    """
    Save the reproducibility checklist to a markdown file.
    """
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(build_checklist_markdown(), encoding="utf-8")
    return path


if __name__ == "__main__":
    saved_path = save_checklist()
    print(f"Checklist saved to: {saved_path}")
