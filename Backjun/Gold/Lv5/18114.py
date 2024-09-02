import sys

input = sys.stdin.readline

N, C = map(int, input().split())

weight = list(map(int, input().split()))
weight.sort()

def binary(left, right, target):
    while left <= right:
        mid = (left + right) // 2
        if weight[mid] == target:
            return True
        if weight[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

def check():
    if C in weight:
        return 1
    start, end = 0, N-1
    while start < end:
        total = weight[start] + weight[end]
        if total == C:
            return 1
        elif total > C:
            end -= 1
        else:
            diff = C - total
            if diff != weight[start] and diff != weight[end] and binary(start, end, diff):
                return 1
            start += 1
    return 0

print(check())

