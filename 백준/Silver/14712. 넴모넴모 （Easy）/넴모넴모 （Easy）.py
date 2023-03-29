"""
네 개가 2 × 2 사각형을 이루는 부분을 찾아 그 위에 있는 “넴모”들을 모두 없애는 것을 질릴 때까지 반복

2×2 격자판에 2×2 사각형을 이루지 않도록 “넴모”들을 배치하는 방법은 
모든 경우(16) 중 네 칸 모두에 “넴모”가 올라가 있는 경우를 제외한 15가지
"""

def DFS(depth): # 제일 끝까지 간 경우가 깊이의 최대
    global cnt

    if depth == N*M:
        cnt += 1
        return 

    x = depth // M + 1
    y = depth % M + 1
    #1 1 / 1 2 / 2 1 / 2 2

    if nemo[x-1][y] == 0 or nemo[x-1][y-1] == 0 or nemo[x][y-1] == 0: # 넴모 놓을 수 있으면
        nemo[x][y] = 1
        DFS(depth+1)
        nemo[x][y] = 0 # 초기화
    DFS(depth+1) # 넴모 안놓았을 때

N, M = map(int, input().split()) # 행의 개수 N, 열의 개수 M
nemo = [[0] * (M+1) for _ in range(N+1)]
cnt = 0 

DFS(0)
print(cnt)