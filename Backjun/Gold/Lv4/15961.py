import sys
from collections import defaultdict

n, d, k, c = map(int, sys.stdin.readline().split())

arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))

left, right = 0, k-1
dict = defaultdict(int)
dict[c] += 1

for i in range(right+1):
    dict[arr[i]] += 1

result = -int(1e9)

while left < n:
    result = max(len(dict), result)
    dict[arr[left]] -= 1

    if (dict[arr[left]] == 0):
        del dict[arr[left]]

    left += 1
    right += 1
    dict[arr[right % n]] += 1

print(result)
