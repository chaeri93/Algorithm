import sys

input = sys.stdin.readline
n = int(input())

arr = [0] * 11
arr[1] = 1
arr[2] = 2
arr[3] = 4

for i in range(4, 11):
    arr[i] = arr[i - 1] + arr[i - 2] + arr[i - 3]

for i in range(0, n):
    t = int(input())
    print(arr[t])