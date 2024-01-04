import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
k = int(input())

graph = [[] for _ in range(n)]
for i in range(n):
    if arr[i] != -1:
        if i != k:
            graph[arr[i]].append(i)


def dfs(a):
    while graph[a]:
        x = graph[a].pop()
        dfs(x)
    graph[a].append(False)


dfs(k)

cnt = 0
for i in range(n):
    if not graph[i]:
        cnt += 1

print(cnt)
