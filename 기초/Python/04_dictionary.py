# -*- coding: utf-8 -*-
print('01_dictionary 생성')
language = {'C':123,'java':55,'python':444}# 키-값 쌍으로 이루어짐.
print(language)
print(language['C'])
test = dict()


print('02_dictionary 자료형')
x = {100:'hundred',False:0, 'test':[1,2,3,4]}
#dictionary key는 시퀀스형을 제외한 정수,실수, 문자열 등이 가능하며,
#dictionary value는 시퀀스형인 리스트 및 딕셔너리도 포함시킬 수 있다.
print(x['test'])

