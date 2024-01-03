import sys

input = sys.stdin.readline

K = int(input())
building = list(map(int, input().split()))
tree = [[] for _ in range(K)]


def Maketree(arr, level):
    mid = len(arr) // 2
    tree[level].append(arr[mid])

    if len(arr) == 1:
        return

    Maketree(arr[:mid], level + 1)
    Maketree(arr[mid + 1:], level + 1)


Maketree(building, 0)

for i in range(K):
    print(*tree[i])
