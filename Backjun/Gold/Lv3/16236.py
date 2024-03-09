from collections import deque

N = int(input())
space = [list(map(int, input().split())) for _ in range(N)]

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

pos = []
for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            pos.append(i)
            pos.append(j)

cnt = 0


def bfs(x, y):
    visited = [[0] * N for _ in range(N)]
    queue = deque([[x, y]])
    candidate = []

    visited[x][y] = 1

    while queue:
        i, j = queue.popleft()

        for idx in range(4):
            ni = i + dx[idx]
            nj = j + dy[idx]

            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                if space[x][y] > space[ni][nj] and space[ni][nj] != 0:
                    visited[ni][nj] = visited[i][j] + 1
                    candidate.append((visited[ni][nj] - 1, ni, nj))
                elif space[x][y] == space[ni][nj] or space[ni][nj] == 0:
                    visited[ni][nj] = visited[i][j] + 1
                    queue.append([ni, nj])

    return sorted(candidate, key=lambda x: (x[0], x[1], x[2]))


i, j = pos
size = [2, 0]
while True:
    space[i][j] = size[0]
    candidate = deque(bfs(i, j))

    if not candidate:
        break
    step, x, y = candidate.popleft()
    cnt += step
    size[1] += 1

    if size[0] == size[1]:
        size[0] += 1
        size[1] = 0

    space[i][j] = 0
    i, j = x, y

print(cnt)
