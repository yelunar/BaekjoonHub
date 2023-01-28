# 일곱 명 키 합이 100

nan = []
one = 0
two = 0

for _ in range(9):
    nan.append(int(input())) # 9난쟁이 변수 선언

sum_nan = sum(nan)

for i in range(8): # 범위 2개 뽑기
    for j in range(i+1, 9):
        if sum_nan - (nan[i]+nan[j]) == 100: # 두개 뺀게 100이면
            one = nan[i]
            two = nan[j]

nan.remove(one) # 변수 두개 제거 하고 더해줌
nan.remove(two)

nan.sort()

for i in nan:
    print(i)
