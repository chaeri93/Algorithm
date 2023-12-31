from collections import deque
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    orders = list(map(int, input().split()))
    original = deque()

    for i in range(1, n + 1):
        curr = orders.pop()
        if curr == 1:
            original.appendleft(i)
        elif curr == 2:
            original.insert(1, i)
        elif curr == 3:
            original.append(i)

    print(*original)
