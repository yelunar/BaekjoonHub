import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline

# N개의 자연수 중에서 M개를 고른 수열
# 이전 값 추가해서 현재넣을값과 같은지 체크해야함
# 중복 수열 안되니까 prev 변수 선언 / visited는 필요없음(중복해서 고를수있어서)
# 비내림차순이니까 s(start) 있어야함 -> 자기자리 부터 고르기 시작해야하니까

def dfs(n, s, lst):
    if n == m : #길이 같으면 종료
        ans.append(lst)
        return 
    
    prev = 0 # 이전 값 저장
    for i in range(s, N): 
        if prev != arr[i]: # 더 큰 조건 안넣어도되는게 그냥 같은값 한개로 돌려서 그런듯..
            prev = arr[i] 
            dfs(n+1, i, lst+[arr[i]])


N, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

ans = []

dfs(0, 0, [])

for i in ans:
    print(*i)