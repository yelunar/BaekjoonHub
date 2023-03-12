import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input()) # 주사위 개수
dice = [list(map(int, input().split())) for _ in range(N)]
ans = 0

for i in range(6):
    cnt = 0

    for j in range(N):
        if i == 0 or i == 5:
            cnt += max(dice[j][1:5])
            if j!= N-1 and i == 0:
                i = dice[j+1].index(dice[j][5])
            elif j != N-1 and i == 5:
                i = dice[j + 1].index(dice[j][0])

        elif i == 1 or i == 3:
            cnt += max(dice[j][0], dice[j][2], dice[j][4], dice[j][5])
            if j != N-1 and i == 1:
                i = dice[j+1].index(dice[j][3])
            elif j != N-1 and i == 3:
                i = dice[j + 1].index(dice[j][1])

        elif i == 2 or i == 4:
            cnt += max(dice[j][0], dice[j][1], dice[j][3], dice[j][5])
            if j != N-1 and i == 2:
                i = dice[j+1].index(dice[j][4])
            elif j != N-1 and i == 4:
                i = dice[j + 1].index(dice[j][2])

    if ans < cnt:
        ans = cnt
print(ans)