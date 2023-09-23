def dfs(x, y):
    if struct[x][y] == "-":
        struct[x][y] = 1
        for _y in [1, -1]:
            Y = y + _y
            if (Y > 0 and Y < m) and struct[x][Y] == '-':
                dfs(x, Y)

    if struct[x][y] == "|":
        struct[x][y] = 1
        for _x in [1, -1]:
            X = x + _x
            if (X > 0 and X < n) and struct[X][y] == '|':
                dfs(X, y)


def solution(n, m, struct):
    count = 0

    for i in range(n):
        for j in range(m):
            if struct[i][j] == "-" or struct[i][j] == "|":
                dfs(i, j)
                count += 1

    return count


n, m = map(int, input().split())
struct = []
for _ in range(n):
    struct.append(list(input()))

print(solution(n, m, struct))
