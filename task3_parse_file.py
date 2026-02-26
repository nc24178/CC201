from pathlib import Path
from task1_parse_single import parse_log_line
LOG_PATH = Path("sample_logs.txt")
def main():
    if not LOG_PATH.exists():
        print("ERROR: sample_logs.txt not found")
        return
    valid = [parse_log_line(line) for line in LOG_PATH.read_text(encoding="utf-8").splitlines() if parse_log_line(line)]
    print("First 5 valid parsed lines:")
    for item in valid[:5]: print(item)
if __name__ == "__main__":
    main()
