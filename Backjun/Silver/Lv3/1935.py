if __name__ == '__main__':
    n = int(input())
    form = input()
    num_lst = [int(input()) for _ in range(n)]

    stk = []

    for i in form:
        if i.isalpha():
            stk.append(num_lst[ord(i)-65])
        else:
            a = stk.pop()
            b = stk.pop()

            if i == '+':
                b += a

            elif i == '-':
                b -= a

            elif i == '*':
                b *= a

            elif i == '/':
                b /= a

            stk.append(b)

    print('%.2f' % stk[-1])