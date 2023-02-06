T = int(input()) # TC

for _ in range(T):
    H, W, N = map(int,input().split()) # 호텔의 층 수, 각 층의 방 수, 몇 번째 손님
    # 6 12 10 -> 402
    hosu = (N // H) + 1
    floor = N % H
    if N % H == 0:  # H의 배수면
            hosu = N // H
            floor = H
    print(floor*100+hosu)