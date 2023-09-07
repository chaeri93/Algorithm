n = int(input())
conferance = list()
for i in range(n):
    x, y = map(int, input().split())
    conferance.append((x, y))
conferance = sorted(conferance, key=lambda x: x[0])
conferance = sorted(conferance, key=lambda x: x[1])

cnt = last = 0
for x, y in conferance:
    if x >= last:
        cnt += 1
        last = y

print(cnt)
