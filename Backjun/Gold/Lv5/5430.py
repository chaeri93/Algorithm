import sys
from collections import deque

input = sys.stdin.readline

if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        func = input()
        n = int(input())
        arr = deque(input().rstrip()[1:-1].split(","))

        flag = 0
        if n == 0:
            arr = []

        for i in func:
            if i == "R":
                flag += 1
            elif i == "D":
                if len(arr) == 0:
                    print("error")
                    break
                else:
                    if flag % 2 == 0:
                        arr.popleft()
                    else:
                        arr.pop()

        else:
            if flag % 2 == 0:
                print("[" + ",".join(arr) + "]")
            else:
                arr.reverse()
                print("[" + ",".join(arr) + "]")

