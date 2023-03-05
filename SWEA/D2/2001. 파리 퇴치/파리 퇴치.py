T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = []
    for i in range(N):
        for j in range(N):
            tmp = 0
            for k in range(M):
                for l in range(M):
                    if 0<= i+k < N and 0<= j+l < N:
                        tmp += arr[i+k][j+l]
            cnt.append(tmp)
    
    ans = max(cnt)
    print(f'#{tc} {ans}')