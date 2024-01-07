import sys

input = sys.stdin.readline
from collections import defaultdict

while True:

    N, K = map(int, input().split())
    if [N, K] == [0, 0]:
        break
    L = list(map(int, input().split()))
    Parent = defaultdict(int)

    index = 0
    for i in range(1, N):
        Parent[L[i]] = L[index]
        if i < N - 1 and L[i] + 1 < L[i + 1]:
            index += 1

    count = 0
    if Parent[Parent[K]]:
        for Node in L:
            if (Parent[Parent[K]] == Parent[Parent[Node]]) and Parent[Node] != Parent[K]:
                count += 1
    print(count)
