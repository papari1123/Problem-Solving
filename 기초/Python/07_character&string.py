# -*- coding: utf-8 -*-
print('00. 문자열이 아닌 자료형의 변환')
de = 'test' + str(2.5)

print('01 문자열 바꾸기')
print('hello world!'.replace('world!','python'))

print('02 문자 바꾸기')
table = str.maketrans('abcde','12345') # abcde 각 문자를 12345로 변환하는 table을 생성
a = 'apple'.translate(table)
print(a)

print('03 문자열 결합 및 분리')
t = ['c','java','python','veilog','go']
t1 =' '.join(t)
t2 = '-'.join(t)
print(t1)
print(t2)
t3 = t1.split()
t4 = t2.split('--')
print(t3[2])
print(t3)
print(t4)

print('04 문자열 연결')
d ='$'.join(t)
print(d)

print('05 대문자와 소문자 전환')
p = 'python'
print(p.upper())
print(p.lower())

print('06 공백 삭제')
test = '   a b c   '
print(test.lstrip()) #왼쪽 공백 삭제
print(test.rstrip()) #오른쪽 공백 삭제
print(test.strip()) #양쪽 공백 삭제

print('07 zero 채우기')
print('55'.zfill(2)) # 숫자 앞에 0을 2개 채움

print('08 문자열 위치 찾기')
test = 'pencil pen'
print(test.find('pe')) #찾는게 없으면 -1 반환

print('09 문자열 개수 세기')
print(test.count('pe'))

print('10 문자열 길이 구하기')
print(len(test))
