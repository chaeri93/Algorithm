N = int(input())

def bt(i):
    answer.append(int(i))
    for j in range(0, int(i[-1])):
        bt(i + str(j))


if N > 1023:  # 갯수가 1023개인듯... 0 부터 9876543210 까지 이므로 얼마 안나옴
    print(-1)
else:
    answer = []
    for i in range(10):  # 맨 앞자리가 0, 1, ,... , 9
        bt(str(i))

    print(sorted(answer)[N - 1])