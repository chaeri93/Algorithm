n = int(input())
system = dict()
for i in range(n):
    a, b = input().split()
    a = int(a)
    if a in system.keys():
        continue
    else:
        system[a] = b

system = dict(sorted(system.items()))

for i in system.keys():
    print(i, system[i])