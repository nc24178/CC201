from task1_parse_single import parse_log_line
LINES = ["2026-02-05 08:11:20 | ERROR | db | DB timeout", "BAD LINE", "2026-02-05 08:11:25 | warn | api | Slow", "2026-02-05 | INFO | auth | ok | EXTRA"]
def parse_lines(lines):
    return [parse_log_line(l) for l in lines if parse_log_line(l) is not None]
if __name__ == "__main__":
    for r in parse_lines(LINES): print(r)
