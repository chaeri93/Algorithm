from collections import deque

n = int(input())
drink = list(map(int, input().split()))

drink = deque(sorted(drink))

ans = 0

while len(drink) > 1:
    drink.append(drink.popleft()/2 + drink.pop())

print(max(drink))