n = int(input())
num_card = set(map(int, input().split()))
#set 자료구조는 해쉬 값을 사용하기 때문에 in 연산자를 사용해 데이터를 찾더라도 O(1)이 나온다.
m = int(input())
nums = list(map(int, input().split()))

for i in nums:
    if i in num_card:
        print(1, end=" ")
    else:
        print(0, end=" ")