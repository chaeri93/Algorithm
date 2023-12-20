from collections import deque

if __name__ == '__main__':
    n = int(input())
    arr = [i for i in range(1, n+1)]
    arr = deque(arr)
    for _ in range(n-1):
        arr.popleft()
        arr.append(arr.popleft())

    print(arr[0])