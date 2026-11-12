import os
from pathlib import Path

src = Path(__file__).with_name("summary.txt")
text = src.read_text(encoding="utf-8").strip()

# The gate accepts only 1..2000 characters with at least one non-space;
# fail loudly here rather than emit an entry the scorer marks invalid.
if not text or len(text) > 2000:
    raise SystemExit(f"summary.txt breaks the gate: {len(text)} characters")

out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
(out_dir / "entry.txt").write_text(text + "\n", encoding="utf-8")
