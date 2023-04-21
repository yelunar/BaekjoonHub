from collections import deque
import sys

T = int(input())
for tc in range(T):
    P = sys.stdin.readline().rstrip()
    N = int(input())
    arr = deque(sys.stdin.readline().rstrip()[1:-1].split(','))

    if N == 0:
        arr = deque()

    count_R = 0
    for word in P:
        if word == 'R':
            count_R += 1
        else:
            if arr:
                # 정배열
                if count_R % 2 == 0:
                    arr.popleft()
                # 역배열
                else:
                    arr.pop()
            else:
                print('error')
                break
    else:
        if count_R % 2 == 0:
            print('[',end='')
            print(','.join(arr),end='')
            print(']')
        else:
            arr.reverse()
            print('[', end='')
            print(','.join(arr), end='')
            print(']')
