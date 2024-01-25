import sys

input = sys.stdin.readline

n = int(input())
stone = [[0, 0]]

for _ in range(n - 1):
    stone.append(list(map(int, input().split())))

dp = [0 for _ in range(n + 1)]
if n == 1:
    print(0)
elif n == 2:
    print(print(stone[1][0]))
else:
    dp[2] = stone[1][0]
    dp[3] = min(stone[1][0] + stone[2][0], stone[1][1])
    for i in range(4, n + 1):
        dp[i] = min(dp[i - 1] + stone[i - 1][0], dp[i - 2] + stone[i - 2][1])
    k = int(input())
    MIN = 9999999
    for i in range(1, n - 2):
        dpcopy = dp[:]
        if dp[i] + k < dp[i + 3]:
            dpcopy[i + 3] = dpcopy[i] + k
            for j in range(i + 4, n + 1):
                dpcopy[j] = min(dpcopy[j], dpcopy[j - 1] + stone[j - 1][0], dpcopy[j - 2] + stone[j - 2][1])
            if MIN > dpcopy[-1]:
                MIN = dpcopy[-1]
    if MIN == 9999999:
        print(dp[-1])
    else:
        print(MIN)
