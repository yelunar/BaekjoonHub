import sys
# sys.stdin = open('input3.txt')

"""
 문자열 그 자체로 회문이면 0, 유사회문이면 1, 그 외는 2를 출력
 <투포인터> => 리스트에 순차적으로 접근해야 할 때 두 개의 점의 위치를 기록하면서 처리
"""

def check_2(words, start, end):
    while start < end:
        if words[start] == words[end]:
            start += 1
            end -= 1
        else:
            return False
    return True

def check(words):
    start = 0
    end = len(words) - 1

    if words == words[::-1]: # 안빼고 회문이면 0 반환
        return 0

    else:
        while start < end: # 첫 지점과 끝 지점이 크로스 될때까지
            if words[start] == words[end]: # 서로 같으면 다음 조사 범위 갱신
                start += 1
                end -= 1 
            else: 
                left = check_2(words, start + 1, end)
                right = check_2(words, start, end - 1)
                if left or right:
                    return 1
                else:
                    return 2


#---------------------------------------
for _ in range(int(sys.stdin.readline())):
    print(check(str(sys.stdin.readline().strip()))) # string 은 굳이 리스트 안에 안넣어도 슬라이싱 되니까 input으로만 받는다
