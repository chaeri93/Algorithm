dp = []

def makeTree(n, links):
    tree = [[] for _ in range(n)]
    for link in links:
        tree[link[0]].append(link[1])
    return tree

def fillDp(sales, tree, node, flag):
    global dp
    if dp[node][flag]!= -1:
        return dp[node][flag]

    if not tree[node]:
        dp[node][flag] = sales[node - 1] if flag else 0
        return dp[node][flag]

    dp[node][flag] = 0
    attend_flag = False
    diff = float('inf')
    for next_node in tree[node]:
        attend = fillDp(sales, tree, next_node, True)
        absent = fillDp(sales, tree, next_node, False)
        dp[node][flag] += min(attend, absent)
        if attend < absent:
            attend_flag = True
        diff = min(diff, attend - absent)

    if flag:
        dp[node][flag] += sales[node - 1]
    elif attend_flag:
        dp[node][flag] += diff
    return dp[node][flag]

def solution(sales, links):
    global dp
    v = len(sales)
    dp = [[-1 for _ in range(2)] for _ in range(v + 1)]
    tree = makeTree(v + 1, links)
    return min(fillDp(sales, tree, 1, True), fillDp(sales, tree, 1, False))
