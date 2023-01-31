t = int(input()) # test case

# 최대공약수 구하고 A, B의 곱을 최대 공약수로 나누면 최소공배수를 구할 수 있음

for i in range(1, t+1):
    a, b = map(int, input().split())
    answer = a*b

    while b>0:
        a,b = b, a%b
    print(answer//a)