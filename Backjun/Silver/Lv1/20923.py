from collections import deque


def solution(m, card):
    temp = [deque(), deque()]
    t = 0
    for _ in range(m):
        temp[t].appendleft(card[t].popleft())
        if not card:
            break
        win = -1
        for i in [0, 1]:
            if temp[i] and temp[i][0] == 5:
                win = 0
        if temp[0] and temp[1] and temp[0][0] + temp[1][0] == 5:
            win = 1
        if win != -1:
            for i in [1 - win, win]:
                while temp[i]:
                    card[win].append(temp[i].pop())
        t = 1 - t

    if len(card[0]) > len(card[1]):
        print('do')
    elif len(card[1]) > len(card[0]):
        print('su')
    else:
        print('dosu')


if __name__ == "__main__":
    n, m = map(int, input().split())

    card = [deque(), deque()]
    for _ in range(n):
        d, s = map(int, input().split())
        card[0].appendleft(d)
        card[1].appendleft(s)

    solution(m, card)
