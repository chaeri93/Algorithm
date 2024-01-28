import sys

input = sys.stdin.readline

n, m = map(int, input().split())

subject = [tuple(map(int, input().split())) for _ in range(m)]
subject.sort()
dp = [1] * (n+1)

for a, b in subject:
    if dp[b] <= dp[a]:
        dp[b] = dp[a] + 1

print(*dp[1:])
