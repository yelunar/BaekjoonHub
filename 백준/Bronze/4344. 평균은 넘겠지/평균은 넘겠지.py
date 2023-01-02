n = int(input())

for i in range (n):
    score = list(map(int, input().split()))
    avg = sum(score[1:])/score[0]
    sdt = 0
    for j in range(1, len(score)):
        if score[j]>avg:
            sdt += 1

    per = ((sdt/score[0])*100)
    print('%.3f' % per + '%')