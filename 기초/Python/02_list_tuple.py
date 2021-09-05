# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 12:24:45 2021
"""
from collections import deque
print('01. 리스트 생성')
a = [0,1,2,3,4] #리스트는 대괄호로 묶고 콤마(,)를 사용한다.
b = ['jame',15,134.3,123,True] # 무슨 자로형이든 상관없이 저장이 가능하다.
c = list() # 빈 리스트의 생성, c = []도 동일하게 적용됨.

print('02. range를 이용한 리스트 초기화')
c = list(range(0,10)) #0부터 9까지 정수를 리스트에 넣음.
d = list(range(2,10,2)) # 0부터 10까지 2씩 증가하는 정수를 리스트에 넣음.

print('03. 듀플의 생성') #저장된 요소를 수정하거나 삭제할 수 없는 읽기 전용 리스트임.
da = (1,2,3,4)
db = 1,2,3,4   # 소괄호 없이 생성가능.
dc = ('abc',1,2,3,4,5) # 자료형 상관없이 생성가능

print('04. range를 사용한 튜플의 생성')
dd = tuple(range(10)) 

print('05. 문자열이 아닌 자료형의 변환')
de = 'test' + str(2.5)

print('06. 문자열 길이 구하기')
df = len(de)
 
########## 리스트와 듀플 응용 #############
print('07. 리스트에 요소 추가, 리스트 확장, 삭제')
a.append(5)
a.extend([1,2])
a.insert(4,500) # 4번째 인덱스에 500 추가
a[2:2] = [500,600] # 2번쨰 인덱스부터 500,600을 추가
a.insert(2,[500,600]) # 2번째 인덱스에 [500,600]추가
print(a)
last = a.pop() #마지막 요소 반환하고 삭제.
print(last)
a.pop(1) #첫번째 요소 삭제 
del a[1] #마찬가지로 첫번째 요소 삭제
a.remove(500) # 특정값 500 삭제
print(a)
print('08. 리스트를 활용한 스택과 큐')
stack = list()
stack.append(1) #1을 추가
stack.append(2) #2를 추가
stack.pop() # last in 제거

queue = list()
queue.append(1) #1을 추가
queue.append(2) #2를 추가
queue.pop(0) # first in 제거 (0번째)
print(queue)
print('09. 덱 만들기 (double ended queue)')
#덱은 양방향으로 삭제가 가능한 큐라고 볼 수 있음.
deque_ = deque([10,20,30])
deque_.append(500) # 오른쪽에 500 추가
deque_.popleft() #덱의 왼쪽 요소 삭제
deque_.pop() #덱의 오른쪽 요소 삭제
print(deque_)

print('10. 특정 값의 인덱스')
print(deque_.index(30))
e = [1,2,3,4,5,6,7,8,9,2,3,4,5,6]
print(e.count(2))

print('11. 리스트 요소 정렬')
e.sort()
f = sorted(e) # e를 정렬하여 새로운 리스트를 반환.
print(e)

print('12. 리스트 요소 삭제')
e.clear()

print('13. 리스트의 할당과 복사')
a = [0,0,0]
b = a  # 이 경우 실제 리스트는 1개 (할당)
c = a.copy() # 이 경우 리스트가 복사됨..
print(a == b,a == c)
print(a is b,a is c)
# a와 b는 같은 객체이기 때문에, b가 변경되면 a도 바뀜.
# a와 c는 다른 객체.
a[2] = 5
print(a,b,c)

print('14. 인덱스와 요소 함께 출력')
arr = [0,1,2,3,4,5,6,7,8,9]
for v in arr:
    print(v)
for i, v in enumerate(arr):
    print(i,v)
for i, v in enumerate(arr, start =1): #index 시작을 1부터
    print(i,v)

print('15. max, min, sum')
print(max(arr))
print(min(arr))
print(sum(arr))

print('16. 리스트 표현식')
a = [i for i in range(5)] # 0~4까지 숫자 생성.
b = list(i*2 for i in range(5))
c = [i for i in range(10) if i%2 == 0] #조건문을 달 수 있음.
d = [i+j for i in range(10) for j in range(10)] # 여러 변수마다 조건문을 달 수 있음.
print(a,b,c,d)

print('17. map을 사용한 리스트')
a = [1,3,4,5.5,6,7,8.8]
a = list(map(int,a))
# *map은 원본 리스트를 변경하지 않고 새 리스트를 생성함.
print(",을 포함한 값 입력")
b = input().split(',') # input().split()의 결과가 문자열 리스트임.
b = map(int, b)
print(b)
c = list(b)
print(c)  

