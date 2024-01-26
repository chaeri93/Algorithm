import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
coin.sort()


dp = [100001 for i in range(k + 1)]
dp[0] = 0

for c in coin:
    for i in range(c, k + 1):  # 현재 갖고 있는 동전 i를 기준으로 i 미만의 값은 갱신될리 없으므로 i부터 시작.
        dp[i] = min(dp[i], dp[i - c] + 1)

if dp[k] == 100001:
    print(-1)
else:
    print(dp[k])
