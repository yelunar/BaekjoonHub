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
    
# 시간초과
# n = int(input()) # 수열길이
# seq = list(map(int, input().split()))

# # 소수만 빼기
# # 합성수 인거 리스트로 받아서 전체 리스트에서 차집합 구함
# not_prime = []

# for num in seq:
#     if num > 1:
#         for j in range(2, num):
#             if num % j == 0:
#                 not_prime.append(num)
            
# real_not_prime = list(set(not_prime))
# prime = [x for x in seq if x not in real_not_prime] #리스트 차집합 구하기

# dble = 1

# for pri in prime:
#     dble *= pri
    
# print(dble)
