import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())

    for _ in range(N):
        brack = list(input())[:-1]
        ans = 0
        for i in brack:
            if i == "(":
                ans += 1
            else:
                ans -= 1
            if ans < 0:
                print("NO")
                break
        if ans > 0:
            print("NO")
        elif ans == 0:
            print("YES")
