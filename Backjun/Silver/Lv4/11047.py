n, k = map(int,input().split())
coin = []
for i in range(n):
    coin.append(int(input()))

coin.reverse()
cnt = 0
for i in coin:
    if k/i != 0:
        cnt += int(k/i)
        k = k%i

print(cnt)