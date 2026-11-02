"""Stitch the numbered notebooks together into Complete Tutorial.ipynb.

Run from the repo root after editing any of the individual notebooks:

    python tools/build_complete.py

The individual notebooks are the source of truth. Don't edit the
complete notebook by hand, your changes will be overwritten.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "Complete Tutorial.ipynb"
SKIP = {"16. Exercises.ipynb"}  # exercises work better on their own


def chapter_number(path):
    match = re.match(r"(\d+)\.", path.name)
    return int(match.group(1)) if match else None


def main():
    chapters = sorted(
        (p for p in ROOT.glob("*.ipynb") if chapter_number(p) is not None and p.name not in SKIP),
        key=chapter_number,
    )

    toc = ["# NumPy Tutorial (all chapters)\n", "\n",
           "This file is generated from the individual notebooks by `tools/build_complete.py`.\n", "\n"]
    toc += [f"- {p.stem}\n" for p in chapters]

    cells = [{"cell_type": "markdown", "metadata": {}, "source": toc}]
    metadata = None
    seen_import = False

    for path in chapters:
        nb = json.loads(path.read_text(encoding="utf-8"))
        metadata = metadata or nb["metadata"]
        for cell in nb["cells"]:
            cell = dict(cell)
            cell.pop("id", None)
            src = "".join(cell["source"])
            # only keep the first bare `import numpy as np` cell
            if cell["cell_type"] == "code" and src.strip() == "import numpy as np":
                if seen_import:
                    continue
                seen_import = True
            cells.append(cell)

    out = {"cells": cells, "metadata": metadata, "nbformat": 4, "nbformat_minor": 4}
    OUTPUT.write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {OUTPUT.name} from {len(chapters)} notebooks ({len(cells)} cells)")


if __name__ == "__main__":
    main()
