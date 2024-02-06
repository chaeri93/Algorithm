from itertools import permutations, chain
from collections import Counter
from collections import deque


def is_palindrome(n):
    # Convert the integer n to a string
    str_n = str(n)
    length = len(str_n)

    # Check if the string is a palindrome
    for i in range(length // 2):
        if str_n[i] != str_n[length - 1 - i]:
            return False
    return True


def solution(S):
    # Convert the string S to a list of characters
    num = [i for i in S]
    result = deque()
    count = Counter(num)
    for i in count.keys():
        for _ in range(count[i] // 2):
            result.appendleft(i)
            result.append(i)

    for i in sorted(count.keys(), reverse=True):
        if count[i] % 2 != 0:
            result.insert(len(result) // 2, i)
            break

    if result[0] == "0" and int(''.join(result)) != 0:
        result = [x for x in result if x != '0']

    # # Generate all possible permutations of the elements in the list num
    # for i in range(1, len(num) + 1):
    #     # Generate permutations one by one and check for palindromes
    #     for perm in permutations(num, i):
    #         tmp = int(''.join(perm))
    #         if is_palindrome(tmp) and tmp > result:
    #             result = tmp
    # total = list(
    #     map(int, chain.from_iterable([list(map(''.join, permutations(num, i))) for i in range(1, len(num) + 1)])))
    # result = []
    #
    # # Filter out duplicates and keep only palindromic numbers
    # for i in sorted(list(set(total))):
    #     if is_palindrome(i):
    #         result.append(i)

    # Convert the result to a string and return the largest palindromic number
    return int(''.join(result))

    # Examples


print(solution("39878"))  # Output: "898"
print(solution("00900"))  # Output: "9"
print(solution("958814354567345765847696425643513245"))  # Output: "0"
print(solution("54321"))  # Output: "5"
