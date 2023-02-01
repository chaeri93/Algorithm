import sys
from collections import deque


def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if v == k:
            return visited[v]
        for i in (v - 1, v + 1, 2 * v):
            if 0 <= i < Max and not visited[i]:
                visited[i] = visited[v] + 1
                q.append(i)


Max = 100001
n, k = map(int, sys.stdin.readline().split())
visited = [0] * Max
print(bfs(n))
