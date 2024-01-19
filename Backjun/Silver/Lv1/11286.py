import heapq
import sys

input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    x = int(input())
    if x == 0:
        if len(arr) >= 1:
            print(heapq.heappop(arr)[1])
        else:
            print(0)
    else:
        heapq.heappush(arr, (abs(x), x))
