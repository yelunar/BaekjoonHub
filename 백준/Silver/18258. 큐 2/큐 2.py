import sys
from collections import deque # 시간초과 해결

N = int(sys.stdin.readline()) # test case 
que = deque([])

for i in range(N):
    order = sys.stdin.readline().split()

    if order[0] == 'push':
        que.append(order[1])

    elif order[0] == 'pop':
        if que:
            print(que.popleft()) # 처음부터 뽑기
        else:
            print(-1)

    elif order[0] == 'size':
        print(len(que))

    elif order[0] == 'empty':
        if not que:
            print(1)
        else:
            print(0)
    
    elif order[0] =='front':
        if que:
            print(que[0])
        else:
            print(-1)
            
    elif order[0] == 'back':
        if que:
            print(que[-1])
        else:
            print(-1)