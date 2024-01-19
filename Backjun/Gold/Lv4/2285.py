import sys

input = sys.stdin.readline

n = int(input())
people = 0
village = []

for _ in range(n):
    a, b = map(int, input().split())
    village.append((a, b))
    people += b
village.sort(key=lambda x: x[0])

count = 0
for a, b in village:
    count += b
    if count >= people / 2:
        print(a)
        break
