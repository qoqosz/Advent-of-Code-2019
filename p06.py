from collections import defaultdict
from functools import lru_cache

# Part 1
graph = defaultdict(set)
planets = set()

with open('p06.txt') as f:
    for line in f:
        k, v = line.strip().split(')')
        graph[k].add(v)
        planets.update([k, v])


@lru_cache(maxsize=None)
def n_orbits(node):
    for k, v in graph.items():
        if node in v:
            return n_orbits(k) + 1

    return 0


print(sum(n_orbits(p) for p in planets))


# Part 2
def bfs_path(start, goal):
    visited = []
    queue = [[start]]

    if start == goal:
        return queue

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node not in visited:
            neighbours = [k for k, v in graph.items() if node in v]
            neighbours.extend(graph[node])

            for neighbour in neighbours:
                new_path = list(path) + [neighbour]
                queue.append(new_path)

                if neighbour == goal:
                    return new_path

            visited.append(node)

    return None


print(len(bfs_path('YOU', 'SAN')) - 3)
