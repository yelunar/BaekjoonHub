n = int(input()) #무게
bag = 0 #가방 개수

while n >= 0:
    if n % 5 == 0: #5의 배수일떄
        bag += int(n//5)
        print(bag)
        break
    
    n -= 3
    bag += 1

else:
    print(-1)