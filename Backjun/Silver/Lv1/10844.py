import sys

input = sys.stdin.readline

n = int(input())

dp = [[0]*10 for _ in range(n+1)]
for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[n]) % 1000000000)


# 앞에 오는 숫자 = 0 )
# dp[자리 수][0] = dp[자리 수 - 1][1]
# ※ dp[1][0] = 0이기 때문에 어차피 결과엔 영향을 미치지 않는다.
# 앞에 오는 숫자 = 1~8 )
# dp[자리 수][앞에 오는 숫자] = dp[자리 수 - 1][앞에 오는 숫자 -1] + dp[자리 수 - 1][앞에 오는 숫자 + 1]
# dp[n][i] = dp[n][i-1] + dp
# 앞에 오는 숫자 =9 )
# dp[자리 수][9] = dp[자리 수 - 1][8]