import argparse

from adventofcode.helper import init, run, run_all


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
    init(year, day)


def handle_run(year, day):
    run(year, day)


def handle_run_all():
    run_all()


if __name__ == "__main__":
    main()
