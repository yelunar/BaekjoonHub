import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

"""
스타트 팀과 링크 팀의 능력치의 차이의 최솟값을 출력
원래 조합으로 풀랬는데 시간 너무 많이 소요될듯
백트래킹 싫어 나도 문어 교수님처럼 잘하고 싶당 ㅠ ㅅ ㅠ
"""

def DFS(depth, idx):
    global mini
    
    if depth == N//2: # 끝까지 가면 능력 구하기
        tmp1, tmp2 = 0, 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]: # 갔으면 1팀
                    tmp1 += arr[i][j]
                elif not visited[i] and not visited[j]: # 안갔으면 2팀
                    tmp2 += arr[i][j]
        
        mini = min(mini, abs(tmp1-tmp2))
        return
    
    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            DFS(depth+1, i+1)
            visited[i] = False

###################################################
        
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [False for _ in range(N)]
mini = 1e9
DFS(0, 0)
print(mini)