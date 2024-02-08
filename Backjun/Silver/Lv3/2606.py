import sys
sys.setrecursionlimit(10 ** 8)
c = int(sys.stdin.readline())
graph = [[] for _ in range(c + 1)]
visited = [False] * (c + 1)
n = int(sys.stdin.readline())
cnt = 0

for _ in range(n):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(v):
    global cnt
    visited[v] = True

    graph[v].sort()
    for i in graph[v]:
        if not visited[i]:
            cnt += 1
            dfs(i)

dfs(1)
print(cnt)
