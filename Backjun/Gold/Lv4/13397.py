def isValid(midValue):
    low = arr[0]
    high = arr[0]
    d = 1

    for i in arr:
        if high < i:
            high = i

        if low > i:
            low = i

        if high - low > midValue:
            d += 1
            low = i
            high = i

    return m >= d

n, m = map(int, input().split())
arr = list(map(int, input().split()))

right = max(arr)
left = 0

result = right
while left <= right:
    mid = (left + right) // 2

    if isValid(mid):
        right = mid - 1
        result = min(result, mid)
    else:
        left = mid + 1

print(result)