import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for i in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

def bfs(v):
    visited = [0] * (n + 1)
    visited[v] = 1
    q = deque([v])
    cnt = 0

    while q:
        last = q.popleft()
        for i in graph[last]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1
                cnt += 1
    return cnt

result = []

for i in range(1, n+1):
    result.append(bfs(i))

for i in range(len(result)):
    if max(result) == result[i]:
        print(i + 1)
