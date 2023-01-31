n , k = map(int,input().split()) # test case
cnt = 0 # 숫자 몇번 지웠는지 체크하는 cnt
arr = [True] * (n+1) # 숫자 지웠는지 체크하는 list 선언

for i in range(2, n+1):

    for j in range(i, n+1, i): 

        if arr[j]:
            arr[j] = False  # list 지우면 False 반환
            cnt += 1

            if cnt == k:
                print(j)
                break
