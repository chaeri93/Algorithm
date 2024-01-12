n = int(input())
k = []
for _ in range(n):
    k.append(int(input()))
k.sort(reverse=True)

ans = 0
for i, x in enumerate(k):
    if x - i > 0:
        ans += x - i

print(ans)
