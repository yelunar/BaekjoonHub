T = int(input()) # tc
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = [] # 합 다 넣을 list

    dx = []
    dy = []

    for i in range(M): # 0 1 2 n=3일때
        for j in range(M):
            dx.append(i)
            dy.append(j)

    cnt = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            
            # cnt = arr[i][j]
            for k in range(M**2):
                x = j +dx[k]
                y = i +dy[k]
                cnt += arr[y][x]

            result.append(cnt)
            cnt = 0

    print(f'#{tc} {max(result)}')