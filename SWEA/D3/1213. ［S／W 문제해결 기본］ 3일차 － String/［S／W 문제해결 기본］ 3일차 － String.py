# 두 개의 문자열 str1과 str2가 주어짐
# 문자열 str1에 포함된 글자들이 str2에 몇 개씩 들어있는지 찾고, 
# 그중 가장 많은 글자의 개수를 출력

T = 10

for tc in range(1, T+1):
    testcase = input()
    str1 = input()
    str2 = input()

    cnt = str2.count(str1)

    print(f'#{tc} {cnt}')