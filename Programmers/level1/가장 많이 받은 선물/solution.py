def solution(friends, gifts):
    answer = 0
    length = len(friends)
    score = [0] * len(friends)

    give = [[0] * length for _ in range(length)]
    for gift in gifts:
        gift = gift.split(" ")
        giver = friends.index(gift[0])
        getter = friends.index(gift[1])

        give[giver][getter] += 1

    for i in range(length):
        for j in range(i + 1, length):
            give_score = give[i][j]
            get_score = give[j][i]

            if (give_score != get_score) and (give_score > 0 or get_score > 0):
                if give_score > get_score:
                    score[i] += 1

                else:
                    score[j] += 1

            else:
                giver_present_score = sum(give[i])
                getter_present_score = sum(give[j])

                for k in range(length):
                    giver_present_score -= give[k][i]
                    getter_present_score -= give[k][j]


                if giver_present_score > getter_present_score:
                    score[i] += 1

                elif giver_present_score < getter_present_score:
                    score[j] += 1

    answer = max(score)
    return answer
