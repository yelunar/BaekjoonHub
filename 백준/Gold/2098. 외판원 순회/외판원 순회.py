import sys
input = sys.stdin.readline
##############################################
def dfs(node = 0, visited = 1):
    if visited == (1 << n) - 1:
        if cost_list[node][0]:
            return cost_list[node][0]
        else:
            return INF

    if dp[node][visited] != -1:
        return dp[node][visited]

    min_set = INF
    for next_node in range(1, n):
        if visited & (1 << next_node):
            continue

        if cost_list[node][next_node] == 0:
            continue

        min_set = min(min_set,
                                dfs(next_node, visited | (1 << next_node)) + cost_list[node][next_node])

    dp[node][visited] = min_set

    return dp[node][visited]

##############################################
INF = int(1e9)

n = int(input())

cost_list = [list(map(int, input().split())) for _ in range(n)]

dp = [[-1 for _ in range(1 << n)] for _ in range(n)]

dfs()
print(dp[0][1])