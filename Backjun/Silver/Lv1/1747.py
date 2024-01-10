import sys

input = sys.stdin.readline


def check(x):
    if x == 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def is_palindrome(x):
    if str(x) == str(x)[::-1]:
        return True
    return False

if __name__ == "__main__":

    n = int(input())
    while True:
        if check(n) and is_palindrome(n):
            print(n)
            break
        else:
            n += 1
