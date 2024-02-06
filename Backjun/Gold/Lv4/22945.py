import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

start, end = 0, n - 1
ans = 0

while start + 1 < end:
    ans = max(ans, (end - start - 1) * min(arr[start], arr[end]))
    if arr[start] < arr[end]:
        start += 1
    else:
        end -= 1

print(ans)
