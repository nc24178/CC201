from pathlib import Path
from task1_parse_single import parse_log_line
LOG_PATH = Path("sample_logs.txt")
def main():
    if not LOG_PATH.exists(): return
    total = valid = invalid = 0
    for line in LOG_PATH.read_text(encoding="utf-8").splitlines():
        total += 1
        if parse_log_line(line): valid += 1
        else: invalid += 1
    print(f"Total lines: {total}")
    print(f"Valid lines: {valid}")
    print(f"Invalid format lines: {invalid}")
if __name__ == "__main__":
    main()
