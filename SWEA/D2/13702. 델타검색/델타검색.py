T = 10
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    answer = 0

    for x in range(N):
        for y in range(N):
            num = data[x][y]
            
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if 0<= nx < N and 0<= ny < N:
                    answer += abs(data[nx][ny] - data[x][y])

    print(f'#{tc} {answer}')    