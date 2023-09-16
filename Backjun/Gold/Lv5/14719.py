def cal_water(c, heights):
    left_max = max(heights[:c])
    right_max = max(heights[c + 1:])

    limit = min(left_max, right_max)
    water = max(0, limit - heights[c])

    return water


def solution(H, W, heights):
    answer = 0

    for i in range(1, W - 1):
        answer += cal_water(i, heights)

    return answer


if __name__ == "__main__":
    H, W = map(int, input().split())
    heights = list(map(int, input().split()))

    print(solution(H, W, heights))
