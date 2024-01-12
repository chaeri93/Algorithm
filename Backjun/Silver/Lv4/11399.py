n = int(input())
p = list(map(int, input().split()))
p.sort()

ans = 0
tmp = []
for i in p:
    tmp.append(i)
    ans += sum(tmp)

print(ans)
