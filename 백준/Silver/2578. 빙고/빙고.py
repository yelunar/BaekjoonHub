import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

def bingo():
    is_bingo = 0

    for lst in arr:
        if lst.count(0) == 5:
            is_bingo += 1
    
    for list in range(5):
        tmp = 0
        for j in range(5):
            if arr[j][list] == 0:
                tmp +=1
        if tmp == 5:
            is_bingo += 1
    
    tmp = 0
    for i in range(5):
        if arr[i][i] == 0:
            tmp += 1
    if tmp == 5:
        is_bingo += 1
    
    tmp2 = 0
    for i in range(5):
        if arr[i][4-i] == 0:
            tmp2 += 1
    if tmp2 == 5:
        is_bingo += 1
    
    return is_bingo

arr = [list(map(int, input().split())) for _ in range(5)]
numbers = []
for _ in range(5):
    numbers += list(map(int, input().split())) # 싹다 하나의 리스트로 받음

cnt = 0
for k in range(25):
    for i in range(5):
        for j in range(5):
            if numbers[k] == arr[i][j]:
                arr[i][j] = 0
                cnt += 1
    
    if cnt >= 12:
        result = bingo()

        if result >= 3:
            print(k+1)
            break