# 첫줄은 항상 1
# 두 번째 줄부터 각 숫자들은 자신의 왼쪽과 오른쪽 위의 숫자의 합으로 구성

T = int(input()) # test case

for tc in range(1, T+1):
    N = int(input()) # 크기
    arr = []
    for i in range(N):
        arr.append(0) # n줄 이중 리스트 생성 [[0], [0], [0]]

    for i in range(N):
        if i == 0:
            arr[0] = '1'

        elif i == 1:
            arr[1] = '1 1'

        else: 
            arr[i] = '1 ' + f'{i} '*(i-1) + '1'

    print(f'#{tc}')
    for j in range(len(arr)):
        print(arr[j])