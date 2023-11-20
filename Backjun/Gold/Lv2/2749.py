M=1000000
P=1500000

N = int(input())

def solution(n):
    a, b = 0, 1

    for _ in range(n):
        a, b = b%M, (a+b)%M
    return a

print(solution(N%P))