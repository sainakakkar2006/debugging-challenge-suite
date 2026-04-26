from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Run one debugging challenge test suite.")
    parser.add_argument("challenge", help="path to a challenge directory")
    parser.add_argument("--impl", default="fixed.py", help="implementation file inside the challenge")
    args = parser.parse_args()

    challenge = Path(args.challenge).resolve()
    if not challenge.is_dir():
        parser.error(f"challenge directory does not exist: {challenge}")
    if not (challenge / args.impl).is_file():
        parser.error(f"implementation does not exist inside challenge: {args.impl}")

    env = os.environ.copy()
    env["CHALLENGE_IMPL"] = args.impl
    completed = subprocess.run(
        [sys.executable, "-m", "pytest", str(challenge)],
        env=env,
        check=False,
    )
    return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())

