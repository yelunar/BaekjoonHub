import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline

# N개의 자연수 중에서 M개를 고른 수열
# 이전 값 추가해서 현재넣을값과 같은지 체크해야함

# s ->  비내림차순 설정
def dfs(n, s, lst):
    if n == m : #길이 같으면 종료
        ans.append(lst)
        return 
    
    prev = 0 # 이전 값 저장
    for i in range(s, N):
        if visited[i] == 0 and prev != arr[i]: # 사용하지 않았고 안썼으면
            prev = arr[i] 
            visited[i] = 1 # 방문표시하고
            dfs(n+1, i+1, lst+[arr[i]])
            visited[i] = 0 # 끝나고 나면 방문표시 해제

N, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

ans = []
visited = [0]*N

dfs(0, 0, [])

for i in ans:
    print(*i)