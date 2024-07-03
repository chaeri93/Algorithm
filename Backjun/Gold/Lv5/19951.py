import sys
input = sys.stdin.readline

n, m = map(int, input().split())

ground = list(map(int, input().split()))

answer = [0 for _ in range(n+1)]

for _ in range(m):
    a, b, k = map(int, input().split())

    answer[a-1] += k
    answer[b] -= k


change = 0
for i in range(n):
    change += answer[i]
    print(ground[i] + change, end=' ')