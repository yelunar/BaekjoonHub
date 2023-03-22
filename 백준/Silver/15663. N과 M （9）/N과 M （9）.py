def dfs(n, tlst):
    if n==M:
        ans.append(tlst)
        return

    prev = 0
    for j in range(N):
        if v[j]==0 and prev!=lst[j]:
            prev=lst[j]
            v[j]=1
            dfs(n+1, tlst+[lst[j]])
            v[j]=0

N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))

ans = []
v = [0]*N
dfs(0, [])

for lst in ans:
    print(*lst)