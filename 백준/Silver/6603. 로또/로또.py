import sys
# sys.stdin = open('input2.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

"""
독일로또 1~49에서 6개 고름


"""
def DFS(idx, cnt):
    if cnt == 6:
        print(*ans)
        return
    
    for i in range(idx, len(arr)):
        if not visited[i]:
            ans.append(arr[i])
            visited[i] = True
            DFS(i+1, cnt+1)
            ans.pop()
            visited[i] = False

while True:

    arr = list(map(int, input().split()))
    if len(arr) == 1:
        exit(0)
    k = arr.pop(0)
    visited= [False] * len(arr)
    ans = []
    ###############################################

    DFS(0,0)
    print(' ')