import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)


def dfs(cur, prev, tree, dp):
    for child in tree[cur]:
        if child == prev:
            continue
        dfs(child, cur, tree, dp)
        dp[cur] += dp[child]


def solution(cur, prev, q, tree, dp):
    dfs(cur, prev, tree, dp)

    for _ in range(q):
        i = int(input())
        print(dp[i])


if __name__ == "__main__":
    n, r, q = map(int, input().split())

    tree = [[] for _ in range(n + 1)]
    dp = [1] * (n + 1)

    for _ in range(n - 1):
        u, v = map(int, input().split())
        tree[u].append(v)
        tree[v].append(u)

    solution(r, 0, q, tree, dp)
