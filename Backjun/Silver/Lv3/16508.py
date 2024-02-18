import sys

input = sys.stdin.readline

in_str = input()
n = int(input())
price = []
in_major = []
for i in range(n):
    p, m = input().split()
    price.append(int(p))
    in_major.append(m)


def wordinbook(word, book, price):
    cnt = 0
    for w in word:
        if w in book:
            cnt += 1
            book = book.replace(w, ' ', 1) # 오려낸 글자는 없애준다
            if cnt == len(word):
                return price
    return sys.maxsize

result = []

for i in range(1 << n):
    search_str = ""
    sum_price = 0
    for j in range(n):
        if (i & 1 << j) != 0:
            search_str += in_major[j]
            sum_price += price[j]
    result.append(wordinbook(in_str, search_str, sum_price))

result = min(result)
if result == sys.maxsize:
    result = -1

print(result)
