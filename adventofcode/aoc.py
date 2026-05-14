import argparse
from pathlib import Path

from adventofcode.helper import (
    MAX_YEAR,
    MIN_YEAR,
    get_auth,
    get_input_file,
    get_max_day,
    run,
    run_all,
)

TEMPLATE = """#!/usr/bin/env python3
import fileinput


def main(inp):
    for l in inp:
        print(l)


if __name__ == '__main__':
    lines = [x.rstrip() for x in fileinput.input()]
    main(lines)
"""


def year_or_all(value):
    """Custom type function to validate 'year' as either an integer or 'all'."""
    if value.lower() == "all":
        return value
    try:
        year = int(value)
        if 2015 <= year <= 2025:
            return year
        else:
            raise argparse.ArgumentTypeError(
                f"Year must be between 2015 and 2025. Got: {year}"
            )
    except ValueError:
        raise argparse.ArgumentTypeError(
            f"Invalid value: {value}. Must be an integer or 'all'."
        )


def main():
    parser = argparse.ArgumentParser(description="Advent of Code CLI")
    subparsers = parser.add_subparsers(dest="command")

    init_parser = subparsers.add_parser("init", help="Init an aoc day")
    init_parser.add_argument("year", type=int)
    init_parser.add_argument("day", type=int)

    run_parser = subparsers.add_parser("run", help="Run an aoc day")
    run_parser.add_argument("year", type=year_or_all)
    run_parser.add_argument("day", type=int, nargs="?", default=None)

    args = parser.parse_args()

    if args.command == "init":
        handle_init(args.year, args.day)
    elif args.command == "run" and args.year == "all":
        handle_run_all()
    elif args.command == "run":
        handle_run(args.year, args.day)
    else:
        parser.print_help()


def handle_init(year, day):
    if not MIN_YEAR <= year <= MAX_YEAR:
        print(f"Invalid year: {year}. Must be between {MIN_YEAR} and {MAX_YEAR}.")
        return

    max_day = get_max_day(year)
    if not 1 <= day <= max_day:
        print(f"Invalid day: {day}. Must be between 1 and {max_day}.")
        return

    root = Path(__file__).parent
    day_dir = root / str(year) / f"day{day}"
    day_dir.mkdir(parents=True, exist_ok=True)

    script_path = day_dir / f"day{day}.py"
    if not script_path.exists():
        script_path.write_text(TEMPLATE)
        print(f"Created {script_path}")
    else:
        print(f"{script_path} already exists")

    input_path = day_dir / "input.txt"
    if not input_path.exists():
        try:
            get_auth()
            res = get_input_file(year, day)
            input_path.write_bytes(res.read())
            print(f"Downloaded {input_path}")
        except Exception as e:
            print(f"Could not download input: {e}", file=__import__("sys").stderr)


def handle_run(year, day):
    run(year, day)


def handle_run_all():
    run_all()


if __name__ == "__main__":
    main()
