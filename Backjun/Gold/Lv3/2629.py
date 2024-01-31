import sys

input = sys.stdin.readline

n, chu_lst = int(input()), list(map(int, input().split()))
m, check_chu_lst = int(input()), list(map(int, input().split()))

dp = [0]
for chu in chu_lst:
    tmp = []
    for i in dp:
        tmp.append(i + chu)
        tmp.append(abs(i - chu))
    dp = list(set((dp + tmp)))

for chu in check_chu_lst:
    print('Y' if chu in dp else 'N', end=' ')
