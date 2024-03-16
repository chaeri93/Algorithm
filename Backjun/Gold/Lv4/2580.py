import sys
input = sys.stdin.readline

SIZE = 9    # 스도쿠 한 행 사이즈
check_row = [[False] * (SIZE + 1) for _ in range(SIZE)] # 각 행의 숫자 존재 여부 체크
check_col = [[False] * (SIZE + 1) for _ in range(SIZE)] # 각 열의 숫자 존재 여부 체크
check_3x3 = [[False] * (SIZE + 1) for _ in range(SIZE)] # 각 3x3 사각형의 숫자 존재 여부 체크

def calc_area(x, y):
    return (x // 3) * 3 + y // 3


def fill_sudoku(cnt, sudoku):
    if cnt == SIZE * SIZE:
        return True

    x, y = cnt // SIZE, cnt % SIZE
    if sudoku[x][y] > 0:
        return fill_sudoku(cnt + 1, sudoku)
    for i in range(1, SIZE + 1):
        if check_row[x][i] or check_col[y][i] or check_3x3[calc_area(x, y)][i]:
            continue
        check_row[x][i] = True
        check_col[y][i] = True
        check_3x3[calc_area(x, y)][i] = True
        sudoku[x][y] = i

        if fill_sudoku(cnt + 1, sudoku):
            return True
        check_row[x][i] = False
        check_col[y][i] = False
        check_3x3[calc_area(x, y)][i] = False

        sudoku[x][y] = 0
    return False


def solution(sudoku):
    answer = [[0] * SIZE for _ in range(SIZE)]
    for i in range(SIZE):
        for j in range(SIZE):
            answer[i][j] = sudoku[i][j]
            if sudoku[i][j] == 0:
                continue
            check_row[i][sudoku[i][j]] = True
            check_col[j][sudoku[i][j]] = True
            check_3x3[calc_area(i,j)][sudoku[i][j]] = True

    fill_sudoku(0, answer)

    return  answer

if __name__ == "__main__":
    # 입력
    sudoku = [list(map(int, input().split())) for _ in range(SIZE)]

    # 연산 & 출력
    for line in solution(sudoku):
        print(*line)  # *list -> 리스트의 요소를 하나씩 풀어서 print()에 인자로 넣어줌
        # print(*[1, 2, 3]) == print(1, 2, 3)