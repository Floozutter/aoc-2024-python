INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
reports = tuple(tuple(map(int, line.split())) for line in raw.strip().splitlines())

def safe(report: tuple[int, ...]) -> bool:
    pairs = tuple(zip(report, report[1:]))
    return all(a < b and b-a < 4 for a, b in pairs) or all(a > b and a-b < 4 for a, b in pairs)

print(sum(map(safe, reports)))
print(sum(safe(r) or any(safe(r[:i]+r[i+1:]) for i in range(len(r))) for r in reports))
