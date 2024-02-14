import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def Bfs(x, y, iscrash, visited, graph):
    # crash 0: 벽안부시고 가는경우, 1: 부신 경우
    q = deque()
    q.append((x, y, iscrash))
    visited[x][y][iscrash] = 1

    while q:
        x, y, iscrash = q.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y][iscrash]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽 안부수고 이동
            if graph[nx][ny] == 0 and visited[nx][ny][iscrash] == 0:
                q.append((nx, ny, iscrash))
                visited[nx][ny][iscrash] = visited[x][y][iscrash] + 1
            # 벽 부수고 이동
            if graph[nx][ny] == 1 and iscrash == 1:
                q.append((nx, ny, iscrash - 1))
                visited[nx][ny][iscrash - 1] = visited[x][y][iscrash] + 1

    return -1


print(Bfs(0, 0, 1, visited, graph))
