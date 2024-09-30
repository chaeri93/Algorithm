import sys
input = sys.stdin.readline

def rotate(sticker):
    return [list(s) for s in zip(*sticker[::-1])]


def put(stick):
    sr, sc = len(stick), len(stick[0])

    for i in range(n-sr+1):
        for j in range(m-sc+1):
            if compare(i, j, sr, sc, stick):
                for x in range(sr):
                    for y in range(sc):
                        notebook[i + x][j + y] += stick[x][y]
                return True
    return False

def compare(i, j, sr, sc, stick):
    for x in range(sr):
        for y in range(sc):
            if notebook[i + x][j+y] == stick[x][y] == 1:
                return False
    return True

n,m,k = map(int, input().split())
stickers = []
notebook = [[0] * m for _ in range(n)]

for _ in range(k):
    r,c = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(r)]
    stickers.append(sticker)


for stick in stickers:
    for _ in range(4):
        if put(stick):
            break
        stick = rotate(stick)

print(sum(map(sum, notebook)))