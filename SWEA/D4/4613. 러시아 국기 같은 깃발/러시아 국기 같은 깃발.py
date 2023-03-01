T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N개의 줄에는 M개의 문자
    words = [input() for _ in range(N)]
    cnt = 0
    cnt_lst = [] # 값 더해줄 애들

    for i in range(N-2):
        white = words[i].count('W')
        cnt += len(words[i]) - white
        tmp = cnt

        for j in range(i + 1, N-1):
            blue = words[j].count('B')
            tmp += len(words[j]) - blue
            cnt2 = tmp

            for k in range(j + 1, N):
                red = words[k].count('R')
                cnt2 += len(words[k]) - red
                
            cnt_lst.append(cnt2)

    answer = min(cnt_lst)
    print(f'#{tc} {answer}')      