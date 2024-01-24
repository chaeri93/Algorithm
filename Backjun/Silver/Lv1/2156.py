import sys

input = sys.stdin.readline

n = int(input())
array = [int(input()) for _ in range(n)]

d = [0] * n
d[0] = array[0]
d[1] = array[0] + array[1]
d[2] = max(array[2] + array[0], array[2] + array[1], d[1])
for i in range(3, n):
    d[i] = max(array[i] + d[i - 2], array[i] + array[i - 1] + d[i - 3], d[i - 1])

print(max(d))
