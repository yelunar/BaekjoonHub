# 첫 줄 최대공약수, 둘째 줄 최소 공배수 print
# 내장함수 안쓰고 풀기

a, b = map(int, input().split()) # test case

def GCD(a, b):
    while b>0:
        a, b = b, a%b
    return a

def LCM(a,b):
    return a*b // GCD(a, b)

print(GCD(a,b))
print(LCM(a,b))