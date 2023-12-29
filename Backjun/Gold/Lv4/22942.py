import sys

if __name__ == '__main__':
    n = int(input())
    circles = []
    for i in range(n):
        x, r = map(int, sys.stdin.readline().split());
        circles.append((x - r, i))
        circles.append((x + r, i))
    circles.sort()

    stk = []
    for c in circles:
        if stk:
            if stk[-1][1] == c[1]:
                stk.pop()
            else:
                stk.append(c)
        else:
            stk.append(c)

    if stk:
        print('NO')
    else:
        print('YES')