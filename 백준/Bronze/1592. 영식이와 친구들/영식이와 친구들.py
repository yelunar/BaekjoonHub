N, M, L = map(int, input().split())
visited = [0] * (N+1)
visited[1] = 1
cnt = 0
start = 1
while True:

    if visited[start] == M:
        print(cnt)
        break
 
    if visited[start] % 2 != 0: # 반시계방향
        start = (start+L)%N
        visited[start] +=1
        cnt += 1
    
    else: # 시계방향
        start = abs((start-L) % N)
        visited[start] += 1
        cnt +=1

# 원형 문제는 나머지로 계산 가능