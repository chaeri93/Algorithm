import heapq
import sys

input = sys.stdin.readline

n = int(input())
card = [int(input()) for _ in range(n)]
heapq.heapify(card)
ans = 0

while len(card) > 1:
    tmp = 0
    a = heapq.heappop(card)
    b = heapq.heappop(card)
    tmp += a + b
    ans += tmp
    heapq.heappush(card, tmp)

print(ans)
