arr = [[0] * 1003 for i in range(1003)] # 도화지
N = int(input()) # 색종이 장수
cnt = [0] * N

for k in range(N):  # 모든 색종이 순회 (종이 번호)
    x, y, width, height = map(int, input().split())
    for i in range(y, y+height):
        for j in range(x, x+width):
            if arr[i][j] != 0: # 이전에 이미 붙인 종이가 있다면
                cnt[arr[i][j]-1] -= 1  # 이전에 붙인 종이의 영역의 넓이 -1
            arr[i][j] = k + 1  # 새 종이 붙이기 (종이 번호로 표시)
            cnt[k] += 1 # 해당 번호의 영역 1 증가

for i in range(N):
    print(cnt[i])