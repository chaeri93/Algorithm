def solution(n):
    if n % 2 != 0:
        return 0
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[2] = 3

    MOD = 1000000007
    for i in range(4, n + 1, 2):
        dp[i] = dp[i-2] * 3

        for j in range(i-4, )
