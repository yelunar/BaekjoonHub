import sys
from collections import deque

T = int(input())

for _ in range(T):
    p = input() # 수행할 함수
    n = int(input()) # 배열 개수
    arr = sys.stdin.readline().rstrip()[1:-1].split(",") 
    # [ ] 괄호 제외해서 가져오고 콤마로 나눠져 있다고 말해줌
    queue = deque(arr)

    rev, front, back = 0, 0, len(queue)-1
    flag = 0
    if n == 0:
        queue = []
        front = 0
        back = 0

    for j in p:
        if j == 'R':
            rev += 1
        elif j == 'D':
            if len(queue) < 1:
                flag = 1
                print("error")
                break
            else:
                if rev % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()
    if flag == 0:
        if rev % 2 == 0: #뒤집는게 짝수면 안뒤집은
            print("[" + ",".join(queue) + "]")
        else: # 홀수면 뒤집음
            queue.reverse()
            print("[" + ",".join(queue) + "]")