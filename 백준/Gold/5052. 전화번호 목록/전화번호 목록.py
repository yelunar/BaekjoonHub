T = int(input())
for _ in range(T): # tc만큼 돌리기
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(input())
    arr.sort()

    ans = True
    for i in range(n-1):
        if arr[i] == arr[i+1][:len(arr[i])]:
        # if arr[i+1].startswith(arr[i]):
            ans = False
            break
    
    if ans:
        print('YES')
    else:
        print('NO')