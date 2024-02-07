import sys

input = sys.stdin.readline

s = input().strip()
lk = []
rk = []
cnt = 0
for i in s:
    if i == 'K':
        cnt += 1
    else:
        lk.append(cnt)
cnt = 0
for i in s[::-1]:
    if i == 'K':
        cnt += 1
    else:
        rk.append(cnt)
rk.reverse()
l, r = 0, len(lk) - 1
ans = 0
while l <= r:
    ans = max(ans, r - l + 1 + 2 * min(lk[l], rk[r]))
    if lk[l] < rk[r]:
        l += 1
    else:
        r -= 1
print(ans)
