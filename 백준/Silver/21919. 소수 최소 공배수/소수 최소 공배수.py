n = int(input()) # 수열길이
seq = list(map(int, input().split()))

prime = []

for num in seq:
    if not num in prime:
        for j in range(2, num):
            tmp = num % j
            if tmp == 0:
                break
        else:
            prime.append(num)
                
if len(prime) == 0:
    print(-1)
else:
    dble = 1
    for pri in prime:
        dble *= pri
    
    print(dble)