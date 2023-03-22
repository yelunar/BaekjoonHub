import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline

# N개의 자연수 중에서 M개를 고른 수열
# 이전 값 추가해서 현재넣을값과 같은지 체크해야함

def dfs(n, lst):
    if n == m : #길이 같으면 종료
        ans.append(lst)
        return 
    
    prev = 0 # 이전 값 저장
    for i in range(N):
        if visited[i] == 0 and prev != arr[i]:
            prev = arr[i]
            visited[i] = 1
            dfs(n+1, lst+[arr[i]])
            visited[i] = 0

N, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

ans = []
visited = [0]*N

dfs(0, [])

for i in ans:
    print(*i)


# def backtracking(s):
    

# # 완전히 틀린 방법
# n, m = map(int, input().split())
# arr = list(map(int, input().split()))
# arr.sort()

# lst = []
# ans = []
# def backtracking(s):

#     if len(lst) == m:
#         # print(*lst)
#         ans.append(lst)
#         # print(ans)
#         return ans
#     else:
#         for i in range(n):
#             lst.append(arr[i]) # 이렇게하면 얕은 복사 일어나서 
#             backtracking(i)
#             lst.pop() # 여기서 리스트가 모조리 사라짐..

# backtracking(arr[0])

# print(ans)