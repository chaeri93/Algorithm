import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())
graph = []
q = deque()

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

    for j in range(m):
        if graph[i][j] == 1:
            q.append([i,j])

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx,ny))

bfs()
cnt = 0
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    cnt = max(cnt, max(i))

print(cnt-1)
