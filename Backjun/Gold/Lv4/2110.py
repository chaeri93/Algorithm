N, C = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort()

start = 1
end = arr[-1] - arr[0]
result = 0

while (start <= end):
    mid = (start + end) // 2
    current = arr[0]
    count = 1
    for i in range(1, len(arr)):
        if arr[i] >= mid + current:
            current = arr[i]
            count += 1
    if count >= C:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
