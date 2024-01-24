from itertools import product, combinations
from collections import Counter

def solution(dice):

    cases = list(combinations(dice, int(len(dice)/2)))
    index = list(combinations([i for i in range(1, len(dice)+1)], int(len(dice)/2)))

    total = [[0]* 3 for i in range(len(cases))]


    for i, case in enumerate(cases):
        temp = dice.copy()
        for c in case:
            temp.remove(c)

        counts_a = Counter(list(product(*list(case))))
        counts_b = Counter(list(product(*list(temp))))
        dict_a = {}
        dict_b = {}
        for key, value in counts_a.items():
            if sum(key) in dict_a.keys():
                dict_a[sum(key)] += value
            else:
                dict_a[sum(key)] = value
        for key, value in counts_b.items():
            if sum(key) in dict_b.keys():
                dict_b[sum(key)] += value
            else:
                dict_b[sum(key)] = value

        for key,val in dict_a.items():
            for k,v in dict_b.items():

                if key > k:
                    total[i][0] += val * v
                elif key < k:
                    total[i][1] += val * v
                else:
                    total[i][2] += val * v


    return list(index[total.index(max(total))])
