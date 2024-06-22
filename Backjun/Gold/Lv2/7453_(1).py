import sys

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

ab, cd = [], []

for i in range(n):
    for j in range(n):
        ab.append(arr[i][0] + arr[j][1])
        cd.append(arr[i][2] + arr[j][3])

ab.sort()
cd.sort()

result = 0
i, j = 0, len(cd) - 1  # i는 ab의 시작점, j는 cd의 끝점(투포인터)

while i < len(ab) and j >= 0:
    if ab[i] + cd[j] == 0:
        ni, nj = i + 1, j - 1
        # ab가 같은게 여러개인경우
        while ni < len(ab) and ab[i] == ab[ni]:
            ni += 1
        # cd가 같은게 여러개인경우
        while nj >= 0 and cd[j] == cd[nj]:
            nj -= 1
        result += (ni - i) * (j - nj)
        i, j = ni, nj
    elif ab[i] + cd[j] > 0:  # cd가 ab보다 더 절댓값이 큰경우
        j -= 1
    else:  # ab가 cd보다 더 절댓값이 큰 경우
        i += 1

print(result)
