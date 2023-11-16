def solution(N, K, obj):
    knapsack = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

    for i in range(1, N+1):
        for j in range(1, K+1):
            weight = obj[i][0]
            value = obj[i][1]

            if j < weight:
                knapsack[i][j] = knapsack[i-1][j]
            else:
                knapsack[i][j] = max(value + knapsack[i-1][j-weight],knapsack[i-1][j])

    return knapsack[N][K]

if __name__ == "__main__":
    N, K = map(int, input().split())
    obj = [[0,0]]
    for _ in range(N):
        obj.append(list(map(int, input().split())))

    print(solution(N, K, obj))