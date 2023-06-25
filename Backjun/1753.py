import sys

v, e = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())-1
dist = [float('inf')]*v
dist[start] = 0

linked = [[] for _ in range(v)]
for _ in range(e):
    a,b,w = map(int, sys.stdin.readline().split())
    