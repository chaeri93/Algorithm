import sys
from collections import Counter
input = sys.stdin.readline

def backtracking(cnt):
    if cnt == len(word):
        print("".join(ans))
        return

    for k in visited:
        if visited[k]:
            visited[k] -= 1
            ans.append(k)
            backtracking(cnt+1)
            visited[k] += 1
            ans.pop()


n = int(input())
for _ in range(n):
    word = sorted(list(map(str, input().strip())))
    ans = []
    visited = {}

    for i in word:
        if i in visited:
            visited[i] += 1
        else:
            visited[i] = 1

    backtracking(0)
