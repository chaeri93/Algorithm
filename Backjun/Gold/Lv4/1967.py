import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def dfs(start, distance):
    for next, next_d in graph[start]:
        if visited[next] == -1:
            visited[next] = distance + next_d
            dfs(next, distance + next_d)


visited = [-1] * (n + 1)
visited[1] = 0
dfs(1, 0)

last_Node = visited.index(max(visited))
visited = [-1] * (n + 1)
visited[last_Node] = 0
dfs(last_Node, 0)

print(max(visited))
