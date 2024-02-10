import sys

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]

for a in range(n):
    b = int(input())
    graph[b].append(a + 1)

visited = [False] * (n + 1)

result = []


def dfs(node, route):
    route.add(node)
    visited[node] = True
    for i in graph[node]:
        if i not in route:
            dfs(i, route.copy())
        else:
            result.extend(list(route))
            return


for i in range(1, n + 1):
    if not visited[i]:
        dfs(i, set([]))
result.sort()

print(len(result))
for i in result:
    print(i)
