# 모두 N개의 같은 길이의 랜선으로 만들고 싶음 K개의 랜선을 잘라서 만들어야함
# K줄에 걸쳐 이미 가지고 있는 각 랜선의 길이가 센티미터 단위의 정수로 입력
# 구하는거 -> N개를 만들 수 있는 랜선의 최대 길이

# 왜 이게 이진탐색인데

K, N = map(int,input().split()) #랜선의 개수 K, 그리고 필요한 랜선의 개수 N
LAN = []

for _ in range(K):
    LAN.append(int(input()))
    # LAN = [802, 743, 457, 539]

start, end = 1, max(LAN)

while start <= end:
    mid = (start + end) // 2
    answer = 0

    for i in LAN:
        answer += i // mid
    
    if answer >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)