from itertools import permutations

def solution(numbers): # 소수 만들기 
    
    def is_prime(num): # 소수 찾기 함수
        if num < 2:
            return False
        
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False  # i로 나누어 떨어지면 소수가 아니므로 False 리턴
            
        return True # False가 리턴되지 않고 for문을 빠져나왔다면 소수이므로 True 리턴

    ans = set() # 중복제거하려고 집합으로 생성

    for i in range(1, len(numbers) + 1):
        for j in permutations(numbers, i):
            if is_prime(int("".join(j))):
                ans.add(int("".join(j))) 

    return len(ans)
    