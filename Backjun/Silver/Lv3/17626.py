N = int(input())
dp = [0,1]

for i in range(2, N+1):
    min_value = 1e9
    j = 1

    while (j**2) <= i:
        min_value = min(min_value, dp[i - (j**2)])
        j += 1

    dp.append(min_value + 1)
print(dp[N])

# 자신의 수에서 그보다 작은 수의 제곱수를 뺀 것의 최소를 구하고 거기에 한개를 더해주면 된다.
