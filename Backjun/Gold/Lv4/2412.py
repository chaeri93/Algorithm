import sys
from collections import deque

input = sys.stdin.readline

n, T = map(int, input().split())
graph = set()
visited = set()
for _ in range(n):
    a, b = map(int, input().split())
    graph.add((a, b))


def bfs():
    q = deque([[0, 0, 0]])
    visited.add((0, 0))

    while q:
        x, y, cnt = q.popleft()

        if y == T:
            return cnt

        for i in range(-2, 3):
            for j in range(-2, 3):
                nx = x + i
                ny = y + j
                if (nx, ny) in graph and (nx, ny) not in visited:
                    q.append([nx, ny, cnt + 1])
                    visited.add((nx, ny))
    return -1


print(bfs())
