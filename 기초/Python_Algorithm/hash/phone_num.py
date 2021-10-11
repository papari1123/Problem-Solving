"""
https://programmers.co.kr/learn/courses/30/lessons/42577

해쉬 문제는 딕셔너리를 써서
key값을 table에 저장한다.

아래 문법이 주요 이용된다.
1. dict[key] = value # key, value 쌍을 dict 에 추가
2. key in dict       # key가 dict에 존재하는지>? 

"""
def solution(phone_book):
    dict_ = {}
    for ele in phone_book:
        dict_[ele] = 1
    for ele in phone_book:
        for i in range(len(ele)): 
            if ele[:i] in dict_: #ele[:i+1] 로 len(ele)까지 포함하면 자기 자신을 검사하게 됨.
                return False
        
    return True