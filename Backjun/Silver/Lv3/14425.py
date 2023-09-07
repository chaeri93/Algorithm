n, m = map(int,input().split())
s = set()
cnt = 0
for i in range(n):
    s.add(input())
for j in range(m):
    t = input()
    if t in s:
        cnt += 1

print(cnt)