import heapq
import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
min_heap, max_heap = [], []
visitied = defaultdict()
for _ in range(n):
    number, diff = map(int, input().split())
    heapq.heappush(min_heap, [diff, number])
    heapq.heappush(max_heap, [-diff, -number])
    visitied[number] = True

m = int(input())
for _ in range(m):
    command = input().split()
    if command[0] == 'recommend':
        if command[1] == "-1":
            while not visitied[min_heap[0][1]]:
                heapq.heappop(min_heap)
            print(min_heap[0][1])
        elif command[1] == "1":
            while not visitied[-max_heap[0][1]]:
                heapq.heappop(max_heap)
            print(-max_heap[0][1])
    elif command[0] == 'solved':
        visitied[int(command[1])] = False
    else:
        while not visitied[min_heap[0][1]]:
            heapq.heappop(min_heap)
        while not visitied[-max_heap[0][1]]:
            heapq.heappop(max_heap)
        visitied[int(command[1])] = True
        heapq.heappush(min_heap, [int(command[2]), int(command[1])])
        heapq.heappush(max_heap, [-int(command[2]), -int(command[1])])
