import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

station = sorted(list(map(int, input().split())))

if k >= n:
    print(0)
    sys.exit()

dist = []
for i in range(1, n):
    dist.append(station[i] - station[i-1])

dist.sort(reverse=True)

for i in range(k-1):
    dist.pop(0)

print(sum(dist))
