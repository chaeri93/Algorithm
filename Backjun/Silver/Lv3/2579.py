def solution(n, s):
    dp = [0] * n
    if len(s) <= 2:  # 계단이 2개 이하일땐 그냥 다 더해서 출력
        return sum(s)
    else:
        dp[0] = s[0]
        dp[1] = s[0] + s[1]
        for i in range(2, n):
            # 1칸 전에서 온 경우(3칸 전 최댓값에서 + 2칸 이동한 1칸 전 값), 2칸 전에서 온 경우(2칸 전의 최댓값) 중 최댓값 + 현재 계단 값
            dp[i] = max(dp[i - 3] + s[i - 1] + s[i], dp[i - 2] + s[i])
        return dp[-1]


if __name__ == "__main__":
    n = int(input())
    s = [int(input()) for _ in range(n)]
    print(solution(n, s))
