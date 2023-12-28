import sys
from itertools import combinations


if __name__ == '__main__':
    string = sys.stdin.readline().rstrip()
    idx_stack, stack, answer = [], [], set() #1

    for idx, v in enumerate(list(string)): #2
        if v == '(': #3
            stack.append(idx)
        elif v == ')': #4
            start = stack.pop()
            end = idx
            idx_stack.append([start, end])

    for i in range(1, len(idx_stack)+1): #5
        for j in combinations(idx_stack, i): #6
            tmp = list(string) #7
            for k in j:
                start, end = k #8
                tmp[start] = ''
                tmp[end] = ''
            answer.add(''.join(tmp)) #9
    for i in sorted(list(answer)): #10
        print(i)