import sys
import time
import subprocess
from pathlib import Path


def main(day):
    if day is not None:
        path = Path(f"day{day}")
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
            path = Path(f"day{day}")
            script_path = path / Path(f"day{day}.py")
            input_path = path / Path("input.txt")
            if script_path.exists():
                if not input_path.exists():
                    print(f"Could not find input file {input_path}, skipped day {day}.",  file=sys.stderr)
                    continue
                run_day(script_path, input_path)


def run_day(script_path, input_path):
    start = time.time()
    res = subprocess.run([sys.executable, script_path, input_path], check=True, stdout=subprocess.PIPE)
    elapsed = time.time() - start
    #print(res.stdout)
    print(f"ran {script_path} in {elapsed:.3f}s")


if __name__ == "__main__":
    day = sys.argv[1] if len(sys.argv) > 1 else None
    main(day)

