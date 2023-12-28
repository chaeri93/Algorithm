if __name__ == '__main__':
    n = int(input())
    tops = list(map(int, input().split()))

    answer = [0] * n
    stack = []

    for i in range(n):
        while stack:
            if tops[stack[-1]] < tops[i]:
                stack.pop()
            else:
                answer[i] = stack[-1] + 1
                break
        stack.append(i)
    print(*answer)