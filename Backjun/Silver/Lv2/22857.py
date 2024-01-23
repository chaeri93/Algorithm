import sys

input = sys.stdin.readline

n, k = list(map(int, input().split()))
s = [0] + list(map(int, input().split()))
dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for k in range(k + 1):
        if s[i] % 2 == 0:
            dp[i][k] = dp[i - 1][k] + 1
        if k != 0 and s[i] % 2:
            dp[i][k] = dp[i - 1][k - 1]

res = []
for i in dp:
    res.append(i[k])
print(max(res))
