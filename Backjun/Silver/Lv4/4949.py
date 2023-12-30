if __name__ == '__main__':
    while True:
        str = input()
        check = []
        answer = 'yes'
        if str == '.':
            break
        for s in str:
            if s == '(' or s == '[':
                check.append(s)
            elif s == ')':
                if not len(check):
                    answer = 'no'
                    break
                else:
                    if check.pop(-1) != '(':
                        answer = 'no'
                        break
            elif s == ']':
                if not len(check):
                    answer = 'no'
                    break
                else:
                    if check.pop() != '[':
                        answer = 'no'
                        break
            else:
                continue
        if len(check):
            answer = 'no'
        print(answer)
