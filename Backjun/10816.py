n = int(input())
my_card = list(map(int, input().split()))
m = int(input())
nums_card = list(map(int, input().split()))
counter = {}

for i in my_card:
    if i in counter:
        counter[i] += 1
    else:
        counter[i] = 1

for i in nums_card:
    if i in counter:
        print(counter[i], end=" ")
    else:
        print(0, end=" ")