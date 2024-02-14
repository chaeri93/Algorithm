import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
zeros = []
ones = []
for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            zeros.append((i, j))
        if grid[i][j] == 1:
            ones.append((i, j))
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
visited = [[False for _ in range(m)] for _ in range(n)]
answer = 0
num = 1
groups = [0 for _ in range(n * m + 1)]


def find_group(y, x):
    q = deque()
    q.append((y, x))
    visited[y][x] = True
    path = [(y, x)]
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and grid[ny][nx] == 1 and not visited[ny][nx]:
                visited[ny][nx] = True
                path.append((ny, nx))
                q.append((ny, nx))
    for y, x in path:
        grid[y][x] = num
    groups[num] = len(path)


for y, x in ones:
    if not visited[y][x]:
        find_group(y, x)
        num += 1
for y, x in zeros:
    result = 1
    near = []
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < n and 0 <= nx < m:
            if grid[ny][nx] not in set(near):
                near.append(grid[ny][nx])
                result += groups[grid[ny][nx]]
    answer = max(answer, result)
print(answer)
