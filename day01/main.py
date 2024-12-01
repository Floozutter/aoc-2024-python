from collections import Counter

INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
l, r = zip(*(map(int, line.split()) for line in raw.strip().splitlines()))

print(sum(abs(b-a) for a, b in zip(sorted(l), sorted(r))))

counts = Counter(r)
print(sum(a*counts[a] for a in l))
