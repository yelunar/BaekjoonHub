import sys
input = sys.stdin.readline
# sys.stdin = open('input3.txt')
# sys.setrecursionlimit(10**6)

"""
 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장
 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기
 화면에 있는 이모티콘 중 하나를 삭제
 =>  1초 
 
 ans =>  S개의 이모티콘을 화면에 만드는데 걸리는 시간의 최솟값 

 왜 BFS 냐면... 최솟값을 가지는데 수행해야하는 작업의 가중치가 같다 
"""
from collections import deque

s = int(input())

que = deque([[1, 0, 0]]) # 현재 이모티콘 개수, 클립보드에 있는 이모티콘 개수, cnt
visited = [[False]*1001 for _ in range(1001)]
visited[1][0] = True

while que:
    now_screen, clipboard, cnt = que.popleft()

    if now_screen == s:
        print(cnt)
        break
    for i in range(3): # 1초에 3번 연산하기 때문에 그냥 나눔
        if i == 0: # 화면에 있는 이모티콘 모두 복사해서 저장
            new_screen, new_clipboard = now_screen, now_screen
        elif i == 1: # 클립보드에 있는 모든 이모티콘 화면에 붙여넣기
            new_screen, new_clipboard = now_screen + clipboard, clipboard
        else: # 화면에 있는 이모티콘 중 하나 삭제
            new_screen, new_clipboard = now_screen -1, clipboard
        
        if new_screen > 1000 or new_screen < 0 or new_clipboard > 1000 or new_clipboard < 0 or visited[new_screen][new_clipboard]:
            continue

        visited[new_screen][new_clipboard] = True
        que.append([new_screen, new_clipboard, cnt + 1])
