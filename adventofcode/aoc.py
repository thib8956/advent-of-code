import argparse
from pathlib import Path
from adventofcode.helper import run, get_input_file, get_auth


TEMPLATE = """#!/usr/bin/env python3
def main(inp):
    for l in inp:
        print(l)


if __name__ == '__main__':
    import fileinput
    lines = [x.rstrip() for x in fileinput.input()]
    main(lines)
"""


def main():
    parser = argparse.ArgumentParser(description="Advent of Code CLI")
    subparsers = parser.add_subparsers(dest="command")

    init_parser = subparsers.add_parser("init", help="Init an aoc day")
    init_parser.add_argument("year", type=int)
    init_parser.add_argument("day", type=int)

    run_parser = subparsers.add_parser("run", help="Run an aoc day")
    run_parser.add_argument("year", type=int)
    run_parser.add_argument("day", type=int, nargs="?", default=None)

    args = parser.parse_args()

    if args.command == "init":
        handle_init(args.year, args.day)
    elif args.command == "run":
        handle_run(args.year, args.day)
    else:
        parser.print_help()


def handle_init(year, day):
    if not 1 <= day <= 25:
        print(f"Invalid day: {day}. Must be between 1 and 25.")
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


if __name__ == "__main__":
    main()
