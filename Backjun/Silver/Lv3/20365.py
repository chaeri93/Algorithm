import sys

input = sys.stdin.readline

n = int(input())
prob = list(input())[:-1]

colors = {'B': 0, 'R': 0}
colors[prob[0]] += 1
for i in range(1, n):
    if prob[i] != prob[i - 1]:
        colors[prob[i]] += 1

ans = min(colors['B'], colors['R']) + 1

print(ans)
