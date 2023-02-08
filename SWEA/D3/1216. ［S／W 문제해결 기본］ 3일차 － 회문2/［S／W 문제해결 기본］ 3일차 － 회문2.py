for tc in range(1, 11):
    T = int(input())
    N = 100
    cnt = 1

    #가로
    row = []
    for i in range(N):
        data = input()
        row.append(data)
       
        for M in range(N, cnt, -1):
            if cnt > M:
                break
            for k in range(N-M+1):
                if data[k:M+k] == data[k:M+k][::-1]:
                    if len(data[k:M+k]) > cnt:
                        cnt = len(data[k:M+k])

    #세로
    col = []
    col_list = ''
    for x in range(N):
        for y in row:
            col_list += y[x]
        col.append(col_list)
        col_list =''

    for col_word in col:
        for M in range(N, cnt, -1):
            if cnt > M:
                break
            for k in range(N-M+1):
                if col_word[k:M+k] == col_word[k:M+k][::-1]:
                    if len(col_word[k:M+k]) > cnt:
                        cnt = len(col_word[k:M+k])

    print(f'#{tc} {cnt}')