from itertools import combinations


def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def solution(nums):
    result = 0
    for i in combinations(nums, 3):
        if isPrime(sum(i)):
            result += 1
    return result
