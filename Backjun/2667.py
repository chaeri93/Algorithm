import sys
sys.setrecursionlimit(10 ** 6)

n = int(sys.stdin.readline())
graph = []
result = []
cnt = 0
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x,y):
    global cnt
    if x < 0 or x >= n or y < 0 or y >= n:
        return

    if graph[x][y] == 1:
        cnt += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            dfs(i, j)
            result.append(cnt)
            cnt = 0

result.sort()
print(len(result))
for r in result:
    print(r)