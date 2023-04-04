import sys
# sys.stdin = open('input2.txt')
# from collections import deque
input = sys.stdin.readline

"""
배열을 돌리거나 할 때 중요한 점은 
하나의 temp 변수를 만들어주고 처음 시작할 때 값을 넣어준 뒤, 
배열을 돌리다 보면 비어있는 배열이 생기는데 
그때 temp변수 안에 저장해두었던 값을 빈 배열에 넣어주면 됨

그리고 안에 있는 배열도 돌려줘야 하기 때문에
n과 m 중에 작은 값은 2로 나눠준 값 만큼 for문을 돌려서 
가장자리부터 안에 있는 배열까지 돌려주는 방식으로 구현
"""

N, M, R = map(int, input().split()) # N×M 크기 
arr = [list(map(int, input().split())) for _ in range(N)]

for _ in range(R):
    for i in range(min(N, M) // 2): # min(N, M) // 2 만큼 안으로 들어가야해!
        # x, y는 돌려지는 배열 중 가장 첫번째 배열 인덱스
        x, y = i, i
        tmp = arr[x][y]

        # 돌리기 시작
        # 안쪽까지 계속 생각해야하니까 N-i ~ M-i까지 범위 설정
        for j in range(i+1, N-i): # 좌
            x = j
            pre_value = arr[x][y]
            arr[x][y] = tmp
            tmp = pre_value

        for j in range(i+1, M-i): # 하
            y = j
            pre_value = arr[x][y]
            arr[x][y] = tmp
            tmp = pre_value

        for j in range(i+1, N-i): # 우
            x = N-j-1
            pre_value = arr[x][y]
            arr[x][y] = tmp
            tmp = pre_value
        
        for j in range(i+1, M-i): # 상        
            y = M-j-1
            pre_value = arr[x][y]
            arr[x][y] = tmp
            tmp = pre_value
        
# ---------------------------------------------------------

for i in range(N):
    for j in range(M):
        print(arr[i][j] , end=" ")
    print()