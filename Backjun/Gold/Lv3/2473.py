import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort()
target = sys.maxsize
answer = [-1,-1,-1]

for i in range(n-2):
    start = i + 1
    end = n-1
    while start < end:
        if abs(arr[i] + arr[start] + arr[end]) < abs(target):
            target = arr[i] + arr[start] + arr[end]
            answer = [arr[i], arr[start], arr[end]]
        if arr[i] + arr[start] + arr[end] < 0:
            start += 1
        elif arr[i] + arr[start] + arr[end] > 0:
            end -= 1
        else:
            break
print(*answer)