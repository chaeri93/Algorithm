n,m,l = map(int, input().split())
arr = [0]+list(map(int, input().split()))+[l]
arr.sort()

start = 1
end = l - 1
answer = 0

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] > mid:
            cnt += (arr[i] - arr[i-1] - 1) // mid
    if cnt > m:
        start = mid + 1
    else:
        answer = mid
        end = mid - 1

print(answer)