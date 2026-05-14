#!/usr/bin/env python3
import os
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

MIN_YEAR = 2015
MAX_YEAR = 2025
ROOTPATH = Path(os.path.dirname(os.path.realpath(__file__)))


def get_max_day(year):
    # starting with 2025, advent of code only has 12 days
    return 25 if year < 2025 else 12


_auth = None


def _load_env_file(env_path: Path) -> dict:
    env = {}
    if not env_path.exists():
        return env
    with open(env_path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                key, value = line.split("=", 1)
                env[key.strip()] = value.strip().strip('"').strip("'")
    return env


def get_auth():
    global _auth
    if _auth is not None:
        return

    _auth = os.environ.get("AOC_SESSION")

    if not _auth:
        env_file = ROOTPATH.parent / ".env"
        env = _load_env_file(env_file)
        _auth = env.get("AOC_SESSION")

    if not _auth:
        raise RuntimeError(
            "AOC_SESSION not set. Either:\n"
            "  - Set AOC_SESSION environment variable, or\n"
            "  - Create a .env file in project root with: AOC_SESSION=your_token"
        )


def get_input_file(year, day):
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    r = urllib.request.Request(url)
    r.add_header("Cookie", f"session={_auth}")
    res = urllib.request.urlopen(r)
    return res


def resolve_paths(year, day):
    path = ROOTPATH / Path(f"{year}/day{day}")
    script_path = path / Path(f"day{day}.py")
    input_path = path / Path("input.txt")
    return script_path, input_path


def run_all():
    for year in range(2015, MAX_YEAR + 1):
        print(f"Running year {year}")
        run(year, None)


def run(year, day):
    if not MIN_YEAR <= year <= MAX_YEAR:
        print(f"Invalid year {year}", file=sys.stderr)
        exit(1)

    if day is not None:
        if not 1 <= day <= get_max_day(year):
            print(f"Invalid day {day}", file=sys.stderr)
            exit(1)

        script_path, input_path = resolve_paths(year, day)
        if not script_path.exists():
            print(f"Invalid day {day}", file=sys.stderr)
            exit(1)
        if not input_path.exists():
            print(f"Downloading input file {input_path}")
            get_auth()
            with open(input_path, "wb") as f:
                res = get_input_file(year, day)
                f.write(res.read())

        run_day(script_path, input_path)
    else:
        for day in range(1, 26):
            script_path, input_path = resolve_paths(year, day)
            if script_path.exists():
                if not input_path.exists():
                    print(f"- downloading input file {input_path}")
                    get_auth()
                    with open(input_path, "wb") as f:
                        res = get_input_file(year, day)
                        f.write(res.read())
                run_day(script_path, input_path)


def run_day(script_path, input_path):
    try:
        print(f"> running {script_path}")
        start = time.time()
        res = subprocess.run(
            [sys.executable, script_path.absolute(), input_path.absolute()],
            check=True,
            stdout=subprocess.PIPE,
            timeout=30,
        )
        elapsed = time.time() - start
        print(res.stdout.decode())
        print(f"> ran {script_path} in {elapsed:.3f}s")
    except subprocess.TimeoutExpired:
        print(f"> timeout {script_path} after 30s", file=sys.stderr)
