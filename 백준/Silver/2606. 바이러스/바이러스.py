def DFS(S):
    global cnt
    visited[S] = 1

    for i in arr[S]:
        if visited[i] == 0:
            DFS(i)
            cnt += 1
    return cnt


N = int(input()) # 컴퓨터 수
ssang = int(input())
arr = [[] for i in range(N+1)]
visited = [0]*(N+1) # 0과 1로 이루어진 방문 리스트
cnt = 0
for _ in range(ssang):
    start, end = map(int, input().split())
    arr[start].append(end) 
    arr[end].append(start) # [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]

print(DFS(1))