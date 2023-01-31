# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램
n = int(input()) # test case
test_case = map(int,input().split())
prime = 0

for i in test_case:
    not_prime = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                not_prime += 1
        if not_prime == 0: # 2~n까지 전체 순환했을때 약수 없으면
            prime += 1 # prime(소수) 개수 +1

print(prime)