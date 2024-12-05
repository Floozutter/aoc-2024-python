from collections import defaultdict

INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
grid = {(i, j): c for i, line in enumerate(raw.strip().splitlines()) for j, c in enumerate(line)}
infgrid = defaultdict(str, grid)

print(sum(
    all(infgrid[k*di+i, k*dj+j] == c for k, c in enumerate("XMAS"))
    for i, j in grid
    for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1))
))

print(sum(
    (
        infgrid[i, j] == "A"
        and {infgrid[i+1, j+1], infgrid[i-1, j-1]} == {"M", "S"}
        and {infgrid[i+1, j-1], infgrid[i-1, j+1]} == {"M", "S"}
    )
    for i, j in grid
))
