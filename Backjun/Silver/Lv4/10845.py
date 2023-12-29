import sys
from collections import deque
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    order = deque([])
    for _ in range(N):
        ord = input().split()
        if ord[0] == "push":
            order.append(ord[1])
        elif ord[0] == "back":
            print(order[-1]) if len(order) > 0 else print(-1)
        elif ord[0] == "size":
            print(len(order))
        elif ord[0] == "empty":
            print(0) if len(order) > 0 else print(1)
        elif ord[0] == "pop":
            print(order.popleft()) if len(order) > 0 else print(-1)
        elif ord[0] == "front":
            print(order[0]) if len(order) > 0 else print(-1)
