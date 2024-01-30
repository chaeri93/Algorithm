import sys

input = sys.stdin.readline

dp = [[0]*2001 for i in range(11)]
dp[0] = [1]*2001
for i in range(1, 11):
    for j in range(1, 2001):
        dp[i][j] = dp[i][j-1]+dp[i-1][j//2]

t = int(input())
for _ in range(t):
    n, m = [int(x) for x in input().split()]
    print(dp[n][m])

# 1.  j 이하의 i개 수를 만드는 방법 개수를 저장할 dp 배열을 생성한다. (모든 테스트케이스에 사용할 수 있도록 n, m의 최대 수로 크기 설정)
# 2. dp 배열의 0번째를 1로 초기화 한다. (0~2001 이하의 0개 수로 로또번호를 만드는 방법은 1가지!)
# 3. 위에서 설명한 dp[i][j] = dp[i][j-1]+dp[i-1][j//2] 점화식을 사용하여 배열을 채운다.
# 4. 각 테스트케이스에서 원하는 값을 dp 배열에서 찾아 출력