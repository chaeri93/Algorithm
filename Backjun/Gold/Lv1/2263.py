import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

inorder_index = [0] * (n + 1)
for i in range(n):
    inorder_index[inorder[i]] = i


def preorder(in_l, in_r, post_l, post_r):
    global inorder, postorder

    if in_l > in_r or post_l > post_r:
        return

    root = postorder[post_r]
    print(root, end=' ')

    in_root = inorder_index[root]
    left = in_root - in_l
    preorder(in_l, in_root - 1, post_l, post_l + left - 1)
    right = in_r - in_root
    preorder(in_root + 1, in_r, post_r - right, post_r - 1)


preorder(0, n - 1, 0, n - 1)