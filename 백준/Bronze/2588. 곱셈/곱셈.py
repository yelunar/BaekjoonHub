A = int(input()) #첫 번쨰 입력 받은 문자: 숫자로 변환
B = input() #두 번째 입력 받은 문자: 문자열 그대로 둠

# 문자열의 인덱스 이용해서 두번째 입력 받은 문자를 하나씩 숫자로 반환하고 A와 곱함
AXB2 = A * int(B[2])
AXB1 = A * int(B[1])
AXB0 = A * int(B[0])
AXB = A * int(B)

print(AXB2, AXB1, AXB0, AXB, sep='\n')
# sep = '\n'으로 줄 바꿈