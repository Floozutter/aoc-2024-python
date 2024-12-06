INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
header, body = raw.strip().split("\n\n")
rules = tuple(tuple(map(int, line.split("|"))) for line in header.split())
updates = tuple(tuple(map(int, line.split(","))) for line in body.split())

def correct(pages: tuple[int, ...]) -> bool:
    indices = {p: i for i, p in enumerate(pages)}
    return not any(a in indices and b in indices and indices[a] > indices[b] for a, b in rules)

print(sum(u[len(u)//2] for u in updates if correct(u)))
