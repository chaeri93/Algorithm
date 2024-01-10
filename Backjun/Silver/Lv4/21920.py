import sys
from math import gcd

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())

    total = 0
    tmp = 0
    for i in range(n):
        if gcd(a[i], x) == 1:
            total += a[i]
            tmp += 1

    print(total/tmp)
