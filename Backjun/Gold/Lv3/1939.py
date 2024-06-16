import sys
from collections import deque

input = sys.stdin.readline

def bfs(weight):
    visited = [0] * (n + 1)
    visited[start] = 1
    q = deque([start])

    while q:
        now = q.popleft()
        if now == end:
            return True
        for nx, ny in graph[now]:
            if not visited[nx] and weight <= ny:
                visited[nx] = 1
                q.append(nx)
    return False


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

start, end = map(int, input().split())

low = 1
high = 1000000000

result = 0

while low <= high:
    mid = (high + low) // 2
    if bfs(mid):
        result = mid
        low = mid + 1
    else:
        high = mid - 1

print(result)
