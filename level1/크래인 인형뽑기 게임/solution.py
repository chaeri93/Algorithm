def solution(board, moves):
    answer = 0
    stack = []
    for m in moves:
        for i in range(len(board)):
            if board[i][m - 1] != 0:
                stack.append(board[i][m - 1])
                board[i][m - 1] = 0

                if len(stack) > 1:
                    if stack[-1] == stack[-2]:
                        # slice 사용하여 제거
                        # stack = stack[:-2]

                        # .pop 사용하여 제거
                        # stack.pop(-1)
                        # stack.pop(-1)

                        # del 사용하여 제거
                        del stack[-2:]
                        answer += 2
                break
    return answer
