# 완전탐색

def solution(answers):
    students = {1: [ 1, 2, 3, 4, 5], 2: [2, 1, 2, 3, 2, 4, 2, 5], 3: [ 3, 3, 1, 1, 2, 2, 4, 4, 5, 5]}
    scores = {1:0, 2:0, 3:0}
    
    for idx, ans in enumerate(answers): # 문제 답의 인덱스와 답을 같이 불러옴
        for key, value in students.items(): # 학생 번호랑 답 같이 불러옴
            if ans == value[idx % len(value)]:
                scores[key] += 1
    
    max_scores = max(scores.values())      
    result = [key for key, value in scores.items() if value == max_scores]
    
    return result

"""
학생들이 찍는 순서를 딕셔너리에 넣고,
문제와 학생을 하나씩 for if문을 이용해서 비교한다. 
맞으면 점수를 올리고 max 값을 출력한다.


enumerate는 인덱스와 값을 모두 for 문에서 사용할 수 있고
파이썬에서는 for문을 사용할 때 변수를 여러개 지정할 수 있다. 

for key value in student.items() 처럼 이는 딕셔너리의 키 값과 밸류 값을 모두 포문으로 돌릴때 짱짱 유용하다. 
만약 student가 딕셔너리가 아닌 리스트라면, 
for key value in zip (student1, student2) 처럼 z
ip()함수를 사용하면 여러 변수를 쓸 수 있다.

"""