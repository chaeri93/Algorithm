def bomb_position():  # 폭탄 위치 찾기
    for i in range(R):
        for j in range(C):
            if bomb[i][j] == 'O':
                temp.append([i, j])


def bomb_BBAM():  # 터뜨리기
    while temp:
        y, x = temp.popleft()
        bomb[y][x] = '.'
        for dy, dx in splash:
            ny, nx = y + dy, x + dx
            if 0 <= ny < R and 0 <= nx < C:
                bomb[ny][nx] = '.'


def bomb_set():  # 폭탄 두기
    for i in range(R):
        for j in range(C):
            if bomb[i][j] == '.':
                bomb[i][j] = 'O'


import sys
from collections import deque

R, C, N = map(int, sys.stdin.readline().split())
bomb = [list(sys.stdin.readline().strip()) for _ in range(R)]
splash = [[1, 0], [-1, 0], [0, 1], [0, -1]]
if N % 2 != 0:
    N -= 1
    while N > 0:
        temp = deque()
        bomb_position()
        bomb_set()
        N -= 1
        if N == 0:
            break
        bomb_BBAM()
        N -= 1
    for i in bomb:
        print(*i, sep='')
else:
    bomb = [['O'] * C for _ in range(R)]
    for i in bomb:
        print(*i, sep='')
