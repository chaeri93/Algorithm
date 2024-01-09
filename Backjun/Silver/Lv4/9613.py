import sys
from math import gcd

input = sys.stdin.readline

if __name__ == "__main__":
    for _ in range(int(input())):
        t = list(map(int, input().split()))
        ans = 0
        for i in range(1, len(t)):
            for j in range(i + 1, len(t)):
                ans += gcd(t[i], t[j])
        print(ans)
