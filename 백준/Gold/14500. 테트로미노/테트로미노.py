import sys
input = sys.stdin.readline
# sys.stdin = open('input3.txt')
# sys.setrecursionlimit(10**6)

"""

"""
moves = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def dfs(x, y, total, cnt):
    global ans
    if cnt == 4:  # 다 방문 완료
        ans = max(ans, total)  # ans 업데이트
        return

    for dx, dy in moves: 
        nx, ny = x + dx, y + dy  

        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:

            if cnt == 2: # ㅗ 모양 만들기 위해 추가 
                visited[nx][ny] = True 
                dfs(x, y, total + arr[nx][ny], cnt + 1)  # 재귀
                visited[nx][ny] = False  # 백트래킹

            visited[nx][ny] = True 
            dfs(nx, ny, total + arr[nx][ny], cnt + 1)  # 재귀
            visited[nx][ny] = False  # 백트래킹

######################################################################

N, M = map(int, input().split())  
visited = [[False for _ in range(M)] for _ in range(N)]  
arr = [list(map(int, input().split())) for _ in range(N)] 

ans = 0 
for r in range(N):
    for c in range(M):
        visited[r][c] = True  
        dfs(r, c, arr[r][c], 1) 
        visited[r][c] = False  # 백트래킹
        
print(ans)  