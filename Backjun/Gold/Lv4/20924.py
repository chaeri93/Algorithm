import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, r = map(int, input().rstrip().split())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

ans = [0, 0]


def dfs(u, p, sum, flag):
    if flag == 0:
        ans[0] = sum
    else:
        ans[1] = max(ans[1], sum)

    if flag == 0 and len(graph[u]) > 2 - int(u == r):
        flag, sum = 1, 0
    for v, w in graph[u]:
        if v == p:
            continue
        dfs(v, u, sum + w, flag)


dfs(r, r, 0, 0)

print(*ans)
