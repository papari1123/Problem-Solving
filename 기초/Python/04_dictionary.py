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

print('03_dictionary 키 생성')
x = {'a':1,'b':2,'c':3}
x.setdefault('d')
x.setdefault('f',100)
print(x['d'],x['f'])

print('04_키의 값 수정')
x.update(a=10)
x.update(a=5,b=3) #여러 개를 콤마로 구분해 수정 가능.
x.update({4:'four'}) # 키가 숫자면, 딕셔너리를 직접 넣어서 수정 가능.
print(x)

print('05 딕셔너리에서 키-값 삭제')
x.pop('a')
print(x)
x.clear() #전체 삭제
print(x)

print('06 딕셔너리에서 키,값 가져오기')
x = {'a':5,'b':23,'c':5,'d':43,'e':21}
print(x.get('a',5)) # 키 a에 해당하는 값을 가져옴. 없으면 5를 반환.
print(x.items()) # 모든 딕셔너리 키-값 쌍을 가져옴.
print(x.keys()) # 키를 모두 가져옴.
print(x.values()) #값을 모두 가져옴.

print('07 반복문으로 키-값 출력')
for i in x: #키만 출력됨.
    print(i,end=' ')
for key, value in x.items(): #키와 값 모두 출력됨.
    print(key,value)
for value in x.values():
    print(value,end=' ') #값만 가져옴.

print('08 반복문을 이용한 딕셔너리 생성')
key = ['a','b','c','d'] #키를 이용한 생성
x = {key:value for key,value in dict.fromleys(keys).items()}
#dict.fromkeys(keys).items()로 키:값 가져옴.
values = [1,2,3,4,5]

