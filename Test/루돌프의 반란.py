import copy
n, m, p, c, d = map(int, input().split())

rx, ry = map(int, input().split())
rx -= 1
ry -= 1
santa = [list(map(int, input().split())) for _ in range(p)]
santa = {s[0]: [s[1] - 1, s[2] - 1] for s in santa}
print(santa)
santa_score = {i + 1: [0, 0] for i in range(p)}



answer = {i + 1 : 0 for i in range(p)}


def calculate_dist(santa):
    dist_rudolf = []
    for s in santa.keys():
        i, j = santa[s]
        dist = abs(i - rx) ** 2 + abs(j - ry) ** 2
        dist_rudolf.append([s, dist, i, j])
    dist_rudolf.sort(key=lambda x: (x[1], -x[2], -x[3]))
    print(f"dist_rudolf: {dist_rudolf}")
    return dist_rudolf


def interaction(x, y, key, dx, dy):
    arr = list(santa.keys())  # deepcopy
    for a in arr:
        if a not in key and [x, y] == santa[a]:
            print(a, santa[a], key)
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n:
                santa[a] = [nx, ny]
                key.append(a)
            else:
                try:
                    answer[a] = santa_score[a][0]
                except TypeError:
                    print("error")
                    print(key, santa_score)
                santa.pop(a)
                santa_score.pop(a)
                break


def bump(key, dx, dy):
    if key == -1:
        for k, v in santa.items():
            if [rx, ry] == v:
                key = k
        mul = c
        print(mul, c)
        santa_score[key][1] = 2
    else:
        mul = d
        santa_score[key][1] = 1
    print(santa[key], dx, dy, mul, key)
    santa_score[key][0] += mul
    x, y = santa[key]
    nx = x + dx * mul
    ny = y + dy * mul
    if 0 <= nx < n and 0 <= ny < n:
        santa[key] = [nx, ny]
        if [nx, ny] in santa.values():
            print(nx, ny)
            interaction(nx, ny, [key], dx, dy)
        return 0
    else:
        answer[key] = santa_score[key][0]
        santa.pop(key)
        santa_score.pop(key)


drx = [-1, 0, 0, 1, 1, -1, 1, -1]
dry = [0, 1, -1, 0, 1, -1, -1, 1]


def move_rudolf():
    tx, ty = dist_rudolf[0][2:]
    result = []
    for i in range(8):
        nrx = rx + drx[i]
        nry = ry + dry[i]
        if 0 <= nrx < n and 0 <= nry < n:
            dist = abs(nrx - tx) ** 2 + abs(nry - ty) ** 2
            result.append([dist, nrx, nry, i])
    result.sort()
    return result[0][1:]


def move_santa():
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    idx = sorted(list(santa.keys()))
    val = list(santa.values())
    for key in idx:
        if not santa_score[key][1]:
            x, y = santa[key]
            move = []
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n and [nx, ny] not in val:
                    dist = abs(nx - rx) ** 2 + abs(ny - ry) ** 2
                    move.append([dist, nx, ny, i])
            move.sort(key= lambda x:(x[0],x[3]))
            print(move, dis_dict[key])
            if len(move) == 0 or dis_dict[key] <= move[0][0]:
                continue
            santa[key] = move[0][1:3]
            val = list(santa.values())
            print(key, santa[key])
            if santa[key] == [rx, ry]:
                i = move[0][3] + 2 - 4 if move[0][3] + 2 >= 4 else move[0][3] + 2
                bump(key, dx[i], dy[i])
        else:
            santa_score[key][1] -= 1


calculate_dist(santa)

for i in range(m):
    print(f"m:{i}")
    if len(santa) == 0:
        break
    dist_rudolf = calculate_dist(santa)
    rx, ry, tmp = move_rudolf()
    print(rx, ry)
    dist_rudolf = calculate_dist(santa)
    dis_dict = {d[0]: d[1] for d in dist_rudolf}

    if [rx, ry] in santa.values():
        bump(-1, drx[tmp], dry[tmp])
    move_santa()
    for k,v in santa_score.items():
        santa_score[k][0] += 1
    print(santa_score)
    print(santa)

for k,v in santa_score.items():
    answer[k] = v[0]

print(*answer.values())
