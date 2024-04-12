from __future__ import annotations

import argparse
import os
import sys

from logoizer._version import __version__
from logoizer.api import logoize


def main(argv: tuple[str, ...] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", action="version", version=f"logoize {__version__}")
    parser.add_argument(
        "--format",
        "-f",
        choices=("png", "svg"),
        default="svg",
        help="format of the logo image",
    )
    parser.add_argument(
        "--theme", "-t", choices=("light", "dark"), default="light", help="logo theme"
    )
    parser.add_argument("--output", "-o", type=str, default=None)
    parser.add_argument("words", type=str, help="words to logoize")

    args = parser.parse_args(argv)

    if args.output is None:
        output = sys.stdout
    elif os.path.exists(args.output):
        parser.exit(status=1, message=f"{args.output}: file exists")

    logoize(args.words.strip(), output, format=args.format, light=args.theme == "light")

    return 0


if __name__ == "__main__":
    SystemExit(main())
