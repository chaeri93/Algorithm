from math import gcd


def LCM(a, b):
    return a * b // gcd(a, b)


if __name__ == "__main__":
    for _ in range(int(input())):
        a, b = map(int, input().split())

        print(LCM(a=a, b=b))
