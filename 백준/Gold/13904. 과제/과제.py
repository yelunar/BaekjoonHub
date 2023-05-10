import sys
input = sys.stdin.readline

"""
그리디 => 여러가지 방법으로 데이터를 정렬해보고 생각하면 좋다!
"""
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)] 
arr.sort(key=lambda x: x[1], reverse=True) # 점수 내림차순으로 정렬
visited = [False] * 10001
ans = 0 # 점수

for day, worth in arr:
    while day > 0 and visited[day]: # 과제할 날짜 탐색함
        day -= 1
    if day == 0: # 과제를 할 날짜가 없으면 패스함
        continue
    else:
        visited[day] = True
        ans += worth

print(ans)