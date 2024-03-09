import sys

input = sys.stdin.readline

n, k = map(int, input().split())
record = [input().split() for _ in range(k)]

def solution(n, record):
    wheel = ['?'] * n
    alphabet = dict()

    a = ord('A')
    for i in range(26):
        alphabet[chr(a + i)] = True

    idx = 0
    for s, alpha in record:
        idx = (idx - int(s)) % n
        # print(wheel, idx)
        if wheel[idx] == alpha:
            continue
        if wheel[idx] != '?' or not alphabet[alpha]:
            return '!'
        wheel[idx] = alpha
        alphabet[alpha] = False

    return ''.join(wheel[idx:] + wheel[:idx])


print(solution(n, record))