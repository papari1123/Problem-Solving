# -*- coding: utf-8 -*-


print('1. 입력값 두 개의 변수에 저장.')
a,b = input().split()
print(a)
print(b)
# 2. 정수변환
a = int(a)

 
print('2. map을 사용한 <형> ')
a,b,c = map(int,input('write three input :').split())
print(a)
print(b)
print(c)

print('3. split 기준 문자열 지정')
a, b, c = map(int,input('write three input with comma').split(','))
 
print('4. 값을 여러 개 출력')
print(a,b,c)

print('5. sep로 값 사이에 문자 넣기')
print(1,2,3, sep  =',')

print('6. end를 이용해 print 문의 끝에 뭐가 출력될지 정할 수 있음')
#  end=''로 아무것도 지정하지 않으면 문자가 붙어서 나옴
print(1,end='')
print(2,end='')
print(3,end='')  

print('7. 빠른 입출력')
sys.stdin.readline().rstrip()