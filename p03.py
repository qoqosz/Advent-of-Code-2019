# Part 1
with open('p03.txt') as f:
    lines = [line.strip().split(',') for line in f]


def coords(line):
    c, x, y = set(), 0, 0

    for move in line:
        dir, len = move[0], int(move[1:])

        dx, dy = 0, 0

        if dir == 'L':
            dx = -1
        if dir == 'R':
            dx = 1
        if dir == 'U':
            dy = 1
        if dir == 'D':
            dy = -1

        for _ in range(len):
            x, y = x + dx, y + dy
            c.add((x, y))

    return c


p1, p2 = map(coords, lines)
print(min(sum(x) for x in (p1 & p2)))

# Part 2
with open('p03.txt') as f:
    lines = [line.strip().split(',') for line in f]


def coords2(line):
    c, x, y, step = {}, 0, 0, 0

    for move in line:
        dir, len = move[0], int(move[1:])

        dx, dy = 0, 0

        if dir == 'L':
            dx = -1
        if dir == 'R':
            dx = 1
        if dir == 'U':
            dy = 1
        if dir == 'D':
            dy = -1

        for _ in range(len):
            x, y, step = x + dx, y + dy, step + 1
            c[(x, y)] = step

    return c


p1, p2 = map(coords2, lines)
crosses = set(p1.keys()) & set(p2.keys())
print(min(p1[x] + p2[x] for x in crosses))