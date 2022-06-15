def solution(lottos, win_nums):
    answer = []
    # 최저순위
    cnt = 7
    # 최고순위
    best = 7
    for i in lottos:
        if i in win_nums:
            cnt -= 1
            best -= 1
        elif i == 0:
            best -= 1
    # 7은 순위에 없기 때문에 6으로 치환
    if best > 6:
        answer.append(6)
    else:
        answer.append(best)
    if cnt > 6:
        answer.append(6)
    else:
        answer.append(cnt)

    return answer


lottos = [0, 0, 0, 0, 0, 0]
win_nums = [38, 19, 20, 40, 15, 25]
solution(lottos, win_nums)
