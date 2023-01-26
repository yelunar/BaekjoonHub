n = int(input()) # 원판 개수

def hanoi(n, pan1, pan2, pan3): #pan: 각 위치의 판(장대) 번호
    if n == 1: #원판이 하나면 그냥 pan1 - pan3으로 옮기면 끝
        print(pan1, pan3) 
    else: 
        hanoi(n-1, pan1, pan3, pan2) # 원판 n-1개를 pan1에서 pan3으로 옮김
        print(pan1, pan3) #제일 밑에 있는 원판을 pan3으로 옮김
        hanoi(n-1, pan2, pan1, pan3) # 가운데 판의 원을 세번째 원으로 이동

print((2**n)-1) # 하노이 탑 이동 총 순서 공식
hanoi(n,1,2,3) # 원반 n개를 1번 판에서 3번 판으로 이동
