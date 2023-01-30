# 문제가 알파벳으로만 들어오면 포켓몬 번호를 말해야 하고, 
# 숫자로만 들어오면, 포켓몬 번호에 해당하는 문자를 출력

import sys

n, m = map(int, input().split()) #test case
poket_index = {}
poket_name = {}

for i in range(1, n+1):
    poket = sys.stdin.readline().strip()
    poket_index[i] = poket
    poket_name[poket] = i

# print(poket_index)
# print(poket_name)


for _ in range(m):
    search = sys.stdin.readline().strip()

    if search.isdigit() == True:
        print(poket_index[int(search)])
    else:
        print(poket_name[search])


# 시간 초과 -> 이유: list를 하나하나 순환하면서 값 찾고 index 호출
# import sys

# n, m = map(int, input().split()) # test case

# data = [sys.stdin.readline().strip() for i in range(n)]

# for _ in range(m):
#     poket = sys.stdin.readline().strip()

#     if poket.isdigit() == True:     #int형일 경우
#         print(data[int(poket)-1])
#     else:                           #str형일 경우
#         print(data.index(poket)+1)
