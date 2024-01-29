import sys

input = sys.stdin.readline

n, m, h = map(int, input().split())
dp = [[1] + [0] * h for i in range(n + 1)]
for i in range(1, n + 1):
    dp[i] = dp[i - 1].copy()
    blocks = list(map(int, input().split()))
    for b in blocks:
        for j in range(b, h + 1):
            dp[i][j] += dp[i - 1][j - b]
print(dp[n][h] % 10007)

# 1. i번째 사람까지 j를 만드는 모든 경우의 수를 저장할 2차원 dp배열 생성. (0을 만드는 경우의 수는 항상 1이기 때문에 1로 초기화)
# 2. 블록을 사용하지 않는 경우, 이전 배열의 경우의 수 그대로 적용되기 때문에 복사한다.
# 3. 각 블록마다 h까지 돌면서 해당 블록을 사용했을 때의 경우의 수를 더한다.
# 4. 마지막 사람까지 계산한 h를 만드는 경우의 수를 출력한다.
