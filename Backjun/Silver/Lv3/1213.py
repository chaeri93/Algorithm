import sys
from collections import Counter

input = sys.stdin.readline

text = input().rstrip()


def solution(text):

    mid = ''
    result = ''

    for key, value in sorted(Counter(text).items()):
        if value % 2 == 1:
            if len(mid) == 1:
                return "I'm Sorry Hansoo"
            mid = key
        result += key * (value // 2)

    return result + mid + result[::-1]

print(solution(text))
