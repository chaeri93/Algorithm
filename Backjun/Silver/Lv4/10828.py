import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    order = []
    for _ in range(N):
        ord, k = map(int, input().split())
        if ord == "push":
            order.append(k)
        elif ord == "top":
            print(order[-1]) if len(order) > 0 else print(-1)
        elif ord == "size":
            print(len(order))
        elif ord == "empty":
            print(1) if len(order) > 0 else print(0)
        elif ord == "pop":
            print(order.pop()) if len(order) > 0 else print(-1)
