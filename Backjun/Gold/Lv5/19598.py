import sys, heapq
input = sys.stdin.readline

N = int(input())
schedules = sorted([list(map(int, input().split())) for _ in range(N)])
room = []
for start, end in schedules:
    if room and room[0] <= start:
        heapq.heappop(room)
    heapq.heappush(room, end)

print(len(room))
