"""
백트레킹 문제는 DFS의 과정에서 조건을 주며 절대 답이 되지 않을 상황을 정의하고, 
그 상황의 경우 탐색을 중단하고 다시 부모 노드로 돌아가 다른 경우를 탐색하게 끔 한다.

N-Queen 2차원 배열로하면 시간초과 => 1차원 배열로 해서 Queen이 있는 열을 1차원 리스트로 넣는다
이유? 같은 줄에 있을리가 없거든 ,, 

"""

def dfs(n):
    global ans
    if n == N: # N 행까지 진행한 경우 -> 성공!
        ans += 1 
        return
    for j in range(N):
        if arr[j] == arr2[n+j] == arr3[n-j] == 0: # 열/ 대각선 모두 Queen 없음
            arr[j] = arr2[n+j] = arr3[n-j] = 1
            dfs(n+1)
            arr[j] = arr2[n+j] = arr3[n-j] = 0

N = int(input()) # N개의 퀸
arr = [0] * N # 각 행이 어느 열에서 선택되었는지 저장될 리스트
arr2 = [0] *(2*N) # 오른쪽 위 대각선 선택되었는지 저장될 리스트
arr3 = [0] *(2*N) # 왼쪽 위 대각선 선택되었는지 저장될 리스트
ans = 0
dfs(0)
print(ans)