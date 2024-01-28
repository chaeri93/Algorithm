import sys

input = sys.stdin.readline

t = int(input())
k = int(input())
coin = [tuple(map(int, input().split())) for _ in range(k)]

dp = [0] * (t + 1)
dp[0] = 1
for c, tmp in coin:
    for money in range(t, 0, -1):
        for i in range(1, tmp + 1):  # 현재 동전 coin의 개수만큼 for문 진행
            if money - c * i >= 0:  # 0원 이상인 경우
                dp[money] += dp[money - c * i]
print(dp[t])
