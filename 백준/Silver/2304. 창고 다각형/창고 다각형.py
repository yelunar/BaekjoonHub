N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort() # 높이, 위치 순으로 기둥 정렬 
# [[2, 4], [4, 6], [5, 3], [8, 10], [11, 4], [13, 6], [15, 8]]

max_val = [0, 0]    # 최대 높이 기둥 찾기
for i in range(N):
    if arr[i][1] > max_val[1]:
        max_val[0] = arr[i][0]
        max_val[1] = arr[i][1]

last = [arr[0][0], arr[0][1]] # 왼쪽 시작 기둥 기준으로 조사 시작
result = 0

# 제일 큰 기둥 기준으로 반반 해줌
# 앞에서 뒤로
for i in range(1, N): # 첫번째 기둥 이미 했으니까 빼고 시작
    if arr[i][1] >= last[1]: # 다음 조사 대상이 마지막 기둥과 높이 같거나 크면
        result += (arr[i][0] - last[0]) * last[1] # 앞에까지 애들 너비 계산해줌
        last = [arr[i][0], arr[i][1]] # 마지막 조사 위치 초기화
    if last[0] == max_val[0]:
        last = [arr[-1][0], arr[-1][1]] # 이제 뒤에서 앞으로 올테니까 기둥 위치 변경해줌
        break

# 뒤에서 앞으로
for i in range(N-2, -1, -1):
    if arr[i][1] >= last[1]:
        result += (last[0] - arr[i][0]) * last[1]
        last = [arr[i][0], arr[i][1]]
    if last[0] == max_val[0]:
        break

result += max_val[1]
print(result)