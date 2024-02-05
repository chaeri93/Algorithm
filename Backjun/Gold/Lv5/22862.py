import sys

input = sys.stdin.readline

n, k = map(int, input().split())
s = list(map(int, input().split()))

end = 0  # 끝 포인터
result = 0  # 짝수로 이루어져 있는 연속한 부분 수열 중 가장 긴 길이(출력값)
tmp = 0  # 현재 짝수 부분 수열의 길이
count = 0  # 지우려는 홀수 카운트

for start in range(n):

    # end를 가능한 만큼 이동
    while (count <= k and end < n):

        if s[end] % 2 == 1:  # 홀수
            count += 1
        else:  # 짝수
            tmp += 1
        end += 1  # 끝 점 이동

        if start == 0 and end == n:
            result = tmp
            break

    if count == k + 1:
        result = max(tmp, result)

    if s[start] % 2 == 1:  # 시작점이 홀수
        count -= 1
    else:  # 시작점이 짝수
        tmp -= 1

print(result)
