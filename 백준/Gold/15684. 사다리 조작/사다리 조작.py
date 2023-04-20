import sys
input = sys.stdin.readline

"""
성환 임포트
사다리 1-2 사이에 연결되어있으면 1열에 2, 2열에 1이라고 표시
그리고 빈곳에서 사다리를 놓을 수 있는경우에 놓는다or안놓는다 => 재귀

ANS => 가로선 개수의 최솟값을 출력한다. 
만약, 정답이 3보다 큰 값이면 -1을 출력한다. 
또, 불가능한 경우에도 -1을 출력
"""

def put():
    # i번 세로선의 결과가 i번이 나오는지 체크
    for i in range(1,n+1):
        col = i
        for row in range(1,h+1):
            if ladder[row][col]: # 오른쪽에 사다리 놓기
                col += 1 # 
            elif ladder[row][col-1]: # 왼쪽에 사다리 놓기
                col -= 1
        if col != i:
            return False
    return True
# --------------------------------------------
def dfs(row, col, cnt):
    global mini

    if put():
        mini = min(mini, cnt)
        return mini

    if cnt == 3 or cnt >= mini:
        return

    for i in range(row, h+1):
        if i == row :
            col = col
        else :
            col = 1
        for j in range(col,n):
            if ladder[i][j] == 0 and ladder[i][j - 1] == 0 and ladder[i][j+1] == 0 :
                ladder[i][j] = 1 # 사다리 놓기
                dfs(i,j+1, cnt + 1)
                ladder[i][j] = 0 # 사다리 취소

####################################################################

n, m, h = map(int, input().split()) # 세로, 가로, 위치 개수
ladder = [[0] *(n+1) for _ in range(h+1)]
mini = sys.maxsize

for _ in range(m):
    a, b = map(int, input().split())
    ladder[a][b] = 1

dfs(1,1,0)

if mini > 3 :
    print(-1)
else:
    print(mini)