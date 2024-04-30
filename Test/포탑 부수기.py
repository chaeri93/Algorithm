from collections import deque

n, m, k = map(int, input().split())

turret = [list(map(int, input().split())) for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def pick(cnt):
    idx = []
    for i in range(n):
        for j in range(m):
            if turret[i][j]:
                idx.append([turret[i][j], cnt, i + j, i, j])
    sorted(idx, key=lambda x : (x[0], x[1], -x[2], -x[3]))
    # print(idx)
    return idx[0][3:], idx[-1][3:]
def lazer_attack(weakest, strongest):
    q = deque([weakest])
    visited = [[0] * m for _ in range(n)]
    visited[weakest[0]][weakest[1]] = 1

    can_attack = False
    while q:
        print(q)
        x, y = q.popleft()
        if [x, y] == strongest:
            can_attack = True
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0:
                nx += n
            elif nx >= n:
                nx -= n
            if ny < 0:
                ny += m
            elif ny >= m:
                ny -= m
            if not turret[nx][ny] or visited[nx][ny]:
                continue
            q.append([nx, ny])
            visited[nx][ny] = 1


def turret_attck():
    return True

def attack(weakest, strongest):
    lazer_attack(weakest, strongest)
    # if not lazer_attack(weakest, strongest):
    #     turret_attck(weakest, strongest)

for i in range(k):
    weakest, strongest = pick(i)
    turret[weakest[0]][weakest[1]] += n + m
    print(weakest, strongest)
    attack(weakest, strongest)



# answer = sum([turret[i][j] for i in range(n) for j in range(m)])
# print(answer)