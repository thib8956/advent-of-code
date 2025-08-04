import argparse
from adventofcode.helper import run, get_input_file


def main():
    parser = argparse.ArgumentParser(description="Advent of Code CLI")
    subparsers = parser.add_subparsers(dest='command')

    # Sous-commande init
    init_parser = subparsers.add_parser('init', help='Init an aoc day')
    init_parser.add_argument('year', type=int)
    init_parser.add_argument('day', type=int)

    # Sous-commande run
    run_parser = subparsers.add_parser('run', help='Run an aoc day')
    run_parser.add_argument('year', type=int)
    run_parser.add_argument('day', type=int)

    args = parser.parse_args()

    if args.command == 'init':
        handle_init(args.year, args.day)
    elif args.command == 'run':
        handle_run(args.year, args.day)
    else:
        parser.print_help()


def handle_init(year, day):
    # TODO initialize directory if needed, download input file and create
    # dayX.py from a template
    raise NotImplementedError("init")


def handle_run(year, day):
    run(year, day)


if __name__ == "__main__":
    main()

