def solution(arr, m, n, tmp, visited, answers):
    if len(tmp) == m:
        answers.append(tmp[:])
        return

    for i in range(len(arr)):
        if not visited[i]:
            visited[i] = True
            tmp.append(arr[i])
            solution(arr, m, n, tmp, visited, answers)
            visited[i] = False
            tmp.pop()

    return answers


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    visited = [False] * n
    answers = []
    result = sorted(list(set(map(tuple, solution(arr, m, n, [], visited, answers)))))

    for i in result:
        print(*i, sep=" ")
