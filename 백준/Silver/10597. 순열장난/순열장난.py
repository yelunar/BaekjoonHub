def DFS(idx):
    global arr

    if idx == len(words):
        print(*arr)
        exit(0)
    
    num1 = int(words[idx])
    if not visited[num1]:
        visited[num1] = 1
        arr.append(num1)
        DFS(idx+1)
        visited[num1] = 0
        arr.pop()
    
    if idx+1 < len(words):
        num2 = int(words[idx:idx+2])
        if num2 <= N and not visited[num2]:
            visited[num2] = 1
            arr.append(num2)
            DFS(idx+2)
            visited[num2] = 0
            arr.pop()

words = input()
visited = [0] *  51
arr = []
if len(words) < 10:
    N = len(words)
else:
    N = 9+(len(words)-9)//2
DFS(0)