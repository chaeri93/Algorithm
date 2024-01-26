import sys

input = sys.stdin.readline

c, n = map(int, input().split())
arr = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

INF = float('inf')
dp = [INF for _ in range(c + 100)]
dp[0] = 0

for cost, num_people in arr:
    for i in range(num_people, c + 100):
        dp[i] = min(dp[i], dp[i - num_people] + cost)

print(min(dp[c:]))
