import sys
import time
import subprocess
from pathlib import Path


def main(year, day):
    if day is not None:
        path = Path(f"{year}/day{day}")
        script_path = path / Path(f"day{day}.py")
        input_path = path / Path("input.txt")
        if not script_path.exists():
            print(f"Invalid day {day}", file=sys.stderr)
            exit(1)
        if not input_path.exists():
            print(f"Could not find input file {input_path}", file=sys.stderr)
            exit(1)
        run_day(script_path, input_path)
    else:
        for day in range(1, 26):
            path = Path(f"{year}/day{day}")
            script_path = path / Path(f"day{day}.py")
            input_path = path / Path("input.txt")
            if script_path.exists():
                if not input_path.exists():
                    print(f"Could not find input file {input_path}, skipped day {day}.",  file=sys.stderr)
                    continue
                run_day(script_path, input_path)


def run_day(script_path, input_path):
    try:
        start = time.time()
        res = subprocess.run([sys.executable, script_path.absolute(), input_path.absolute()], check=True, stdout=subprocess.PIPE, timeout=30)
        elapsed = time.time() - start
        #print(res.stdout)
        print(f"ran {script_path} in {elapsed:.3f}s")
    except subprocess.TimeoutExpired:
        print(f"timeout {script_path} after 30s", file=sys.stderr)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print(f"Usage: {__file__} <year> [<day>]", file=sys.stderr)
        exit(1)
    year = sys.argv[1] 
    day = sys.argv[2] if len(sys.argv) > 2 else None
    main(year, day)

