if __name__ == '__main__':
    brack = input()
    stack = []
    cnt = 0
    for i in range(len(brack)):
        if brack[i] == "(":
            stack.append("(")
        else:
            if brack[i - 1] == "(":
                stack.pop()
                cnt += len(stack)

            else:
                stack.pop()
                cnt += 1

    print(cnt)
