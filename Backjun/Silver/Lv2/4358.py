import sys

input = sys.stdin.readline

total = 0
dic = dict()
while True:
    tree = input().rstrip()
    if tree == '':
        break
    if tree in dic.keys():
        dic[tree] += 1
    else:
        dic[tree] = 1
    total += 1

dic = dict(sorted(dic.items()))

for w, c in dic.items():
    print("%s %.4f" % (w, c / total * 100))
