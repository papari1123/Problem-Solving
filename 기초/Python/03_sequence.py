# -*- coding: utf-8 -*-
print('01_특정값이 있는지 확인')
a = [0,1,2,3,4,5,6,7,8,9]
print(30 in a)
print(5 in a)
print(5 not in a) #없는지 확인
print('02_시퀀스 객체 연결')
a = [1,2,3,4]
b = [5,6,7,8]
c = a + b
print(c)

print('03_시퀀스_길이')
print(len(c))

print('04 음수인덱스를 이용한 출력')
print(c[-1])

print('05 인덱스 슬라이스')
print(a[0:5]) # 0~4까지 출력
print(a[2:-1]) # 2부터 뒤에서 두번째까지 출력
print(c[0:5:2]) # 0부터 시작해서 2씩 인덱스 증가, 5가 끝.
print(c[2:]) # 2부터 끝까지 슬라이스
print(c[:6:2]) # 첫 요소부터 2씩 증가하여 6까지
print(c[2::2]) # 2부터 2씩  끝요소까지 확인

print('06 del로 슬라이스 삭제')
d = [0,1,2,3,4,5,6,7,8,9,10]
del d[2:5]  
print(d)

