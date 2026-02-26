import json
from pathlib import Path
from task1_parse_single import parse_log_line
LOG_PATH = Path("sample_logs.txt")
OUT_PATH = Path("parsed_logs.json")
def main():
    if not LOG_PATH.exists(): return
    output = []
    for line in LOG_PATH.read_text(encoding="utf-8").splitlines():
        p = parse_log_line(line)
        if p:
            output.append({"timestamp": p[0], "level": p[1], "service": p[2], "message": p[3]})
    OUT_PATH.write_text(json.dumps(output, indent=2), encoding="utf-8")
    print(f"Wrote {len(output)} records to {OUT_PATH}")
if __name__ == "__main__":
    main()
