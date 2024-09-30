from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, ch, d = map(int, input().split())
board = []

cx, cy = -1, -1
for i in range(n):
    board.append(list(input().strip()))
    if cx == -1:
        for j in range(n):
            if board[i][j] == 'S':
                cx, cy = i, j

def dfs(i, j):
    q = deque([[i, j, ch, 0, 0]])  # 체력, 우산 유무, 거리
    visited = [[0] * n for _ in range(n)]
    visited[i][j] = ch
    while q:
        x, y, h, u, cnt = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < n:
                nh, nu = h, u
                if board[nx][ny] == 'E':
                    return cnt + 1

                if board[nx][ny] == 'U':
                    nu = d

                if nu:
                    nu -= 1
                else:
                    nh -= 1

                if nh == 0:
                    continue

                if visited[nx][ny] < nh:
                    visited[nx][ny] = nh
                    q.append([nx, ny, nh, nu, cnt+1])
    return -1


print(dfs(cx, cy))
