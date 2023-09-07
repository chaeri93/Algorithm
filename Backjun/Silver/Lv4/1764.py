n, m = map(int,input().split())
see =set()
hear = set()
for i in range(n):
    see.add(input())
for i in range(m):
    hear.add(input())
result = sorted(list(see&hear))
print(len(result))
for i in result:
    print(i)
