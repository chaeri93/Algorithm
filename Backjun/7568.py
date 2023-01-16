n = int(input())
arr = []
for i in range(n):
    w, h = map(int, input().split())
    arr.append((w, h))

for i in arr:
    r = 1
    for j in arr:
        if i[0] < j[0] and i[1] < j[1]:
            r += 1
    print(r, end=" ")