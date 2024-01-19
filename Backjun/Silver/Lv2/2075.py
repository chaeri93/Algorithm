import heapq
import sys

input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    nums = list(map(int, input().split()))
    if i == 0:
        for n in nums:
            heapq.heappush(arr, n)
    else:
        for n in nums:
            if n > arr[0]:
                heapq.heappop(arr)
                heapq.heappush(arr, n)

print(arr[0])