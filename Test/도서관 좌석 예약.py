"""
EPPER 도서관 좌석 예약
https://level.goorm.io/exam/100917/%EB%8F%84%EC%84%9C%EA%B4%80-%EC%A2%8C%EC%84%9D-%EC%98%88%EC%95%BD/quiz/1
"""


def solution(s, e, N):
    answer = 0
    tmp = [[i, j] for i, j in zip(s, e)]
    tmp.sort(key=lambda x: (x[1], x[1]-x[0]))
    e1 = e2 = -1

    for t in tmp:
        print(t, e1, e2)
        if e1 <= t[0]:
            answer += 1
            e1 = t[1]
        elif e2 <= t[0]:
            answer += 1
            e2 = e1
            e1 = t[1]

    return answer


if __name__ == '__main__':
    n = int(input())
    s = list(map(int,input().split(" ")))
    e = list(map(int,input().split(" ")))
    answer = solution(s, e, n)
    print(answer)
