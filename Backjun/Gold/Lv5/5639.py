import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline


def postOrder(left, right, tree, result):
    if left > right:
        return

    root = tree[left]
    tmp = left + 1

    for i in range(left + 1, right + 1):
        if tree[i] > root:
            tmp = i
            break

    postOrder(left + 1, tmp - 1, tree, result)
    postOrder(tmp, right, tree, result)

    result.append(root)


def solution(tree):
    result = []
    postOrder(0, len(tree) - 1, tree, result)
    return result


if __name__ == "__main__":
    tree = []
    while True:
        try:
            tree.append(int(input()))
        except:
            break

    # 연산
    result = solution(tree)

    # 출력
    for i in result:
        print(i)
