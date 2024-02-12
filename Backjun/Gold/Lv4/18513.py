from collections import deque
import sys

read = sys.stdin.readline

n, k = map(int, read().strip().split())  # 샘터, 집 개수
sam = list(map(int, read().strip().split()))  # 샘터 위치

# 메모리 초과 발생 가능성 때문에 배열이 아닌 딕셔너리를 이용
# key : 위치, value : 불행도
dic = {}
q = deque()

for s in sam:
    dic[s] = 0  # 샘터 위치는 불행도 0으로 dic에 저장
    q.append(s)  # 큐에 샘터 위치 저장


house = 0  # 설치한 집의 개수 카운트할 변수
total = 0  # 설치한 집들의 불행도의 총 합

while q:
    cnt = q.popleft()
    rc = cnt + 1  # cnt 기준 오른쪽으로 1만큼 떨어진 곳
    lc = cnt - 1  # cnt 기준 왼쪽으로 1만큼 떨어진 곳

    if rc not in dic.keys():  # rc에 아무것도 없는 경우
        dic[rc] = dic[cnt] + 1  # rc에서의 불행도 = cnt에서의 불행도 + 1
        house += 1  # 현재까지 가장 불행도가 작은 곳이므로 rc에 집 건설
        total += dic[rc]  # 설치한 집의 불행도 total에 누적
        if house >= k:
            break
        q.append(rc)  # 설치한 집의 개수가 k개 미만이라면 rc 큐에 삽입

    if lc not in dic.keys():  # rc의 경우와 동일
        dic[lc] = dic[cnt] + 1
        house += 1
        total += dic[lc]
        if house >= k:
            break
        q.append(lc)
print(total)
