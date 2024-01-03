import sys

input = sys.stdin.readline

n = int(input())

graph = [[] for i in range(n+1)]

for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = int(input())

for _ in range(q):
    t, k = map(int, input().split())
    if t == 1:
        if len(graph[k]) < 2:
            print("no")
        else:
            print("yes")
    elif t == 2:
        print("yes")