"""
Arg parsing, calling other functions.
"""
import argparse
import os
import sys
from pathlib import Path

from . import round_trip, format_and_display, format_and_write


parser = argparse.ArgumentParser()
parser.add_argument("file", help="file to parse", nargs="*")
parser.add_argument(
    "-w", "--write", help="overwrite file with formatted output", action="store_true"
)
parser.add_argument(
    "-t", "--width", help="set custom width", type=int, required=False, default=80
)
parser.add_argument(
    "--use-yaml-1-1", help="force yaml output to version 1.1", action="store_true"
)
parser.add_argument(
    "-i", "--indent", help="set indent for formatted output", default=2, type=int
)
parser.add_argument(
    "-a", "--ansible", help="set newline style for ansible", action="store_true"
)
args = parser.parse_args()


def main():
    if args.write and not args.file:
        parser.error("write requires at least one file")

    if not args.file:
        # input is piped in.
        round_trip(sys.stdout, sys.stdin, args.width, args.use_yaml_1_1)
        sys.exit(0)

    files = []
    for file in args.file:
        file_path = Path(file)
        if file_path.is_dir():
            files += list(file_path.glob('**/*.yml'))
            files += list(file_path.glob('**/*.yaml'))
        else:
            files.append(file_path.as_posix())

    for file in files:
        if args.write:
            # write to temp file then overwrite
            format_and_write(file, args.width, args.use_yaml_1_1, args.ansible)
        else:
            # write output to standard out
            format_and_display(file, args.width, args.use_yaml_1_1, args.ansible)


if __name__ == "__main__":
    sys.exit(main())
