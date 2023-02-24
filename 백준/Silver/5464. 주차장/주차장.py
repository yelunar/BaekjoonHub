from collections import deque

N, M = map(int, input().split())
cost_queue = deque() #단위 무게당 요금 (인덱스도 이용해봐!)
# s번째 줄에는 주차 공간 s의 단위 무게당 요금 Rs

car_weight = deque()
# 차량들은 1 부터 M 까지 번호로 구분
# M개의 줄 중 k번째 줄에는 차량 k의 무게를 나타내는 정수 Wk

car_order = deque()
# 양수는 들어오는거 / 음수는 나가는거

car_wait = deque()

visited = [0] * N # 지금 주차장 쓰고잇는지 알려줌

answer = 0

for i in range(N):
    cost_queue.append(int(input().strip()))

for j in range(M):
    car_weight.append(int(input().strip()))

for k in range(2*M):
    order = int(input().strip())

    if order > 0:
        if 0 in visited:
            for i in range(N):
                if visited[i] == 0:
                    visited[i] = order
                    break
        else:
            car_wait.append(order)
    else:
        x = visited.index(-order)
        visited[x] = 0
        mini_answer = car_weight[-order-1] * cost_queue[x]
        answer += mini_answer
        if car_wait:
            visited[x] = car_wait.popleft()

print(answer)
    