import sys
input = sys.stdin.readline

def backtracking(cnt, ans):
    global result
    if cnt == 11:
        result = max(result, ans)
        return
    for i in range(11):
        if player[i] or not power[cnt][i]:
            continue
        player[i] = 1
        backtracking(cnt + 1, ans + power[cnt][i])
        player[i] = 0

t = int(input())

for _ in range(t):
    power = [list(map(int, input().split())) for _ in range(11)]
    player = [0] * 11

    result = 0
    backtracking(0,0)
    print(result)

