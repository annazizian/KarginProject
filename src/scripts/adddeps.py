import sys
from pathlib import Path

base_path = Path(__file__).resolve().parent.parent.as_posix()
if base_path not in sys.path:
    sys.path.append(base_path)
