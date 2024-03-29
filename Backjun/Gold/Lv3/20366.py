import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
ans = 100000
for i in range(N):
    for j in range(i + 3, N):
        left, right = i + 1, j - 1
        while left < right:
            tmp = (arr[i] + arr[j]) - (arr[left] + arr[right])
            if abs(ans) > abs(tmp):
                ans = abs(tmp)
            if tmp < 0:
                right -= 1
            else:
                left += 1
print(ans)
