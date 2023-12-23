import sys
from collections import deque
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    arr = deque(enumerate(map(int, input().split())))
    answer = []

    while arr:
        idx, paper = arr.popleft()
        answer.append(idx + 1)

        if paper > 0:
            arr.rotate(-(paper - 1))
        elif paper < 0:
            arr.rotate(-paper)

    print(' '.join(map(str, answer)))