import sys

input = sys.stdin.readline

target = int(input())

n = int(input())

broken = list(map(int, input().split()))

cnt = abs(target - 100)

for i in range(1000001):
    i = str(i)

    for j in range(len(i)):
        if int(i[j]) in broken:
            break
        elif j == len(i) - 1:
            cnt = min(cnt, abs(int(i) - target) + len(i))


print(cnt)


