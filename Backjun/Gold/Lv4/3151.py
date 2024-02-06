import sys
from collections import Counter

n = int(sys.stdin.readline())
arr = sorted(list(map(int, sys.stdin.readline().split())))
cnt_ = Counter(arr)
result = 0

for i, a in enumerate(arr):
    left, right = i + 1, n - 1
    while left < right:
        sum_ = arr[left] + arr[right] + arr[i]
        # 1. 점수 총합이 0인 경우, 같은 값이 있는 것에 대한 처리 필요
        if sum_ == 0:
            #  left값과 right 값이 같은 경우 해당 범위 저장. -4 -4 2 2 2
            if arr[left] == arr[right]:
                result += right - left
                        # 다른 경우 right 값에 대한 개수 합
            else:
                result += cnt_[arr[right]]
            left += 1
                # 2. 점수 총합이 0 보다 큰 경우
        elif sum_ > 0:
            right -= 1
                # 3. 점수 총합이 0 보다 작은 경우
        elif sum_ < 0:
            left += 1

print(result)
