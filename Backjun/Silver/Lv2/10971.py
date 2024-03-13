import sys

input = sys.stdin.readline

ans = 1e8


def backtracking(n, cnt, now, cost):
    global ans, visited, matrix
    if cnt == n:
        if matrix[now][0] != 0:
            ans = min(ans, cost + matrix[now][0])
        return
    if cost >= ans:
        return
    for i in range(n):
        if not visited[i] and matrix[now][i]:
            visited[i] = True
            backtracking(n, cnt + 1, i, cost + matrix[now][i])
            visited[i] = False


def solution(n, cost):
    global ans, visited, matrix
    visited = [False] * n
    matrix = cost

    visited[0] = True
    backtracking(n, 1, 0, 0)

    return ans


if __name__ == "__main__":
    # 입력
    n = int(input())
    cost = [list(map(int, input().split())) for _ in range(n)]
    answer = solution(n, cost)
    print(answer)
