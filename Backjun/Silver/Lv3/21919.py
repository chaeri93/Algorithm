import sys

input = sys.stdin.readline

def check(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


if __name__ == "__main__":
    n = int(input())
    a = set(map(int, input().split()))

    ans = 1
    for i in a:
        if check(i):
            ans *= i

    print("-1") if ans == 1 else print(ans)