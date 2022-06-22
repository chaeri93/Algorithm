import heapq


def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        mixed = heapq.heappop(scoville) + heapq.heappop(scoville)*2
        heapq.heappush(scoville, mixed)
        if len(scoville) == 1 and scoville[0] < K:
            return -1
        cnt += 1

    return cnt

solution([1, 2, 3, 9, 10, 12], 7)