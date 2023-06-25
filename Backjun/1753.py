import heapq
import sys

v, e = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())
INF = int(1e9)
dist = [INF]*(v+1)

linked = [[]*(v+1) for _ in range(v+1)]
for _ in range(e):
    a,b,w = map(int, sys.stdin.readline().split())
    linked[a].append((b,w))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        d, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if dist[now] < d:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in linked[now]:
            cost = d + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(k)

for i in range(1, v+1):
    if dist[i]==INF:
        print("INF")
    else:
        print(dist[i])
    