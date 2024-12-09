INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
grid = {(i, j): c for i, line in enumerate(raw.strip().splitlines()) for j, c in enumerate(line)}

def patrol(grid: dict[tuple[int, int], str]) -> None | int:
    i, j = next(pos for pos, c in grid.items() if c == "^")
    di, dj = -1, 0
    visited: set[tuple[int, int, int, int]] = set()
    while (i, j) in grid:
        if (i, j, di, dj) in visited:
            return None
        visited.add((i, j, di, dj))
        front = i+di, j+dj
        if grid.get(front) == "#":
            di, dj = dj, -di
        else:
            i, j = front
    return len({(i, j) for i, j, _, _ in visited})

print(patrol(grid))
print(sum(patrol(grid | {(i, j): "#"}) is None for (i, j), c in grid.items() if c == "."))
