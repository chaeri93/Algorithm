import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()

    answer = float('inf')
    cnt = 0
    for i in range(n):
        start = i + 1
        end = n - 1
        while start <= end:
            mid = (start + end) // 2
            total = arr[i] + arr[mid]
            if abs(total - k) == answer:
                cnt += 1
            elif abs(total - k) < answer:
                answer = abs(total - k)
                cnt = 1
            if total > k:
                end = mid - 1
            elif total == k:
                break
            else:
                start = mid + 1
    print(cnt)

