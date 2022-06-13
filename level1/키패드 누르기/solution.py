def solution(numbers, hand):
    answer = ''
    # 키패드를 좌표로 변경
    dic = {1: [0, 0], 2: [0, 1], 3: [0, 2],
           4: [1, 0], 5: [1, 1], 6: [1, 2],
           7: [2, 0], 8: [2, 1], 9: [2, 2],
           '*': [3, 0], 0: [3, 1], '#': [3, 2]}
    leftH = dic['*']
    rightH = dic['#']

    for n in numbers:
        current = dic[n]
        # 1, 4, 7을 누르는 경우 왼손
        if n in [1, 4, 7]:
            answer += 'L'
            leftH = current
        # 3, 6, 9를 누르는 경우 오른손
        elif n in [3, 6, 9]:
            answer += 'R'
            rightH = current
        # 2, 5, 8, 0을 누르는 경우
        else:
            # 좌표 거리 계산해주기
            leftD = abs(current[0] - leftH[0]) + abs(current[1] - leftH[1])
            rightD = abs(current[0] - rightH[0]) + abs(current[1] - rightH[1])

            # 왼손이 더 가까운 경우
            if leftD < rightD:
                answer += 'L'
                leftH = dic[n]
            # 오른손이 더 가까운 경우
            elif leftD > rightD:
                answer += 'R'
                rightH = dic[n]
            # 두 손의 거리가 같은 경우
            else:
                # 왼손잡이 경우
                if hand == 'left':
                    answer += 'L'
                    leftH = dic[n]
                # 오른손잡이 경우
                else:
                    answer += 'R'
                    rightH = dic[n]
    return answer
