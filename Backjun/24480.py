import sys
sys.setrecursionlimit(10 ** 8)

n, m, r = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
result = [0] * (n + 1)
cnt = 1


def dfs(v):
    global cnt
    visited[v] = cnt

    graph[v].sort(reverse=True)
    for i in graph[v]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)


for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)


dfs(r)

for i in range(n + 1):
    if i != 0:
        print(visited[i])
