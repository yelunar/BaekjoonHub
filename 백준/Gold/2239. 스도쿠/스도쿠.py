import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10000)

"""

"""

def garo(x, num):
    for y in range(9):
        if arr[x][y] == num:
            return False
    return True

def sero(y, num):
    for x in range(9):
        if arr[x][y] == num:
            return False
    return True

def square(x, y, num):
    nx = (x//3) * 3
    ny = (y//3) * 3
    for i in range(3):
        for j in range(3):
            if arr[nx+i][ny+j] == num:
                return False
    return True

def dfs(depth):
    if depth == len(zeros):
        for xx in range(9):
            for yy in range(9):
                print(arr[xx][yy], end="")
            print()
        exit()
    
    nx, ny = zeros[depth]	
    for num in range(1, 10):
        if garo(nx, num) and sero(ny, num) and square(nx, ny, num):
            arr[nx][ny] = num
            dfs(depth + 1)
            arr[nx][ny] = 0

##############################################################

arr = []
zeros = [] # 0 위치
for x in range(9):
    arr.append(list(map(int, input().rstrip())))
    for y in range(9):
        if arr[x][y] == 0:
            zeros.append((x, y))
dfs(0)