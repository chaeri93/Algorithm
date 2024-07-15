import sys

input = sys.stdin.readline

n, k = map(int, input().split())

# k 가 5보다 작으면 어떤 언어도 배울 수 없음
if k < 5:
    print(0)
    exit()
# k 가 26이면 모든 언어를 배울 수 있음
elif k == 26:
    print(n)
    exit()

answer = 0
words = [set(input().rstrip()) for _ in range(n)]
learn = [0] * 26

for c in ('a', 'c', 'i', 'n', 't'):
    learn[ord(c) - ord('a')] = 1

def dfs(idx, cnt):
    global answer
    if cnt == k-5:
        tmp = 0
        for word in words:
            check = True
            for w in word:
                if not learn[ord(w)-ord('a')]:
                    check = False
                    break
            if check:
                tmp += 1
        answer = max(answer, tmp)
        return
    for i in range(idx, 26):
        if not learn[i]:
            learn[i] = True
            dfs(i, cnt + 1)
            learn[i] = False


dfs(0,0)
print(answer)
