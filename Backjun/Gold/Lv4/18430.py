import sys

input = sys.stdin.readline

N, M = map(int, input().split())


def backtracking(i, j, sum):
    global answer
    if j == M:
        i += 1
        j = 0
    if i == N:
        answer = max(answer, sum)
        return
    if not visited[i][j]:
        for k in range(4):
            a, b, c, d = shape[k]
            x, y, nx, ny = i + a, j + b, i + c, j + d
            if 0 <= x < N and 0 <= nx < N and 0 <= y < M and 0 <= ny < M and not visited[x][y] and not visited[nx][ny]:
                visited[i][j] = visited[x][y] = visited[nx][ny] = True
                backtracking(i, j + 1, sum + board[i][j] * 2 + board[x][y] + board[nx][ny])
                visited[i][j] = visited[x][y] = visited[nx][ny] = False

    backtracking(i, j + 1, sum)


board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

shape = {0: [0, -1, 1, 0], 1: [-1, 0, 0, -1], 2: [-1, 0, 0, 1], 3: [0, 1, 1, 0]}
answer = 0
backtracking(0, 0, 0)
print(answer)
