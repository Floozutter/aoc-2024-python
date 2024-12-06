INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
header, body = raw.strip().split("\n\n")
rules = tuple(tuple(map(int, line.split("|"))) for line in header.split())

def order(pages: tuple[int, ...]) -> tuple[int, ...]:
    pages_before: dict[int, set[int]] = {p: set() for p in pages}
    used_rules = filter(lambda rule: rule[0] in pages_before and rule[1] in pages_before, rules)
    for a, b in used_rules:
        pages_before[b].add(a)
        parents = filter(lambda p: b in pages_before[p], pages_before)
        for p in parents:
            pages_before[p].add(a)
    return tuple(sorted(pages, key = lambda p: len(pages_before[p])))

initial_updates = tuple(tuple(map(int, line.split(","))) for line in body.split())
ordered_updates = tuple(map(order, initial_updates))

print(sum(o[len(o)//2] for i, o in zip(initial_updates, ordered_updates) if i == o))
print(sum(o[len(o)//2] for i, o in zip(initial_updates, ordered_updates) if i != o))
