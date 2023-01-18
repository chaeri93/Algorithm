import sys
from collections import deque

sys.setrecursionlimit(10 ** 8)

n, m, r = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited_dfs = [0] * (n + 1)
visited_bfs = [0] * (n + 1)

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
    graph[u].sort()
    graph[v].sort()

def dfs(v):
    print(v, end=' ')
    visited_dfs[v] = 1
    for i in graph[v]:
        if visited_dfs[i] == 0:
            dfs(i)

def bfs(v):
    visited_bfs[v] = 1
    q = deque([v])
    while q:
        last = q.popleft()
        print(last, end=" ")
        for i in graph[last]:
            if visited_bfs[i] == 0:
                q.append(i)
                visited_bfs[i] = 1

dfs(r)
print()
bfs(r)