#세트는 집합을 표현하는 자료형임.

print('01 세트 만들기')
fruits = {'apple','grape','orange'} # 직접 넣기
apple = set('apple') #set(iterable) -> 중복되지 않는 a,p,l,e가 담김.
five = set(range(5)) # 0,1,2,3,4가 담김
#주의할 것은 아래와 같은 경우 딕셔너리가 만들어짐
dic = {} 
#세트는 요소의 순서가 정해져 있지 않으므로, 세트를 출력하면 매번 요소의 순서는 다르게 나옴.
# 따라서 아래와 같이 대괄호로 요소 출력 불가함.
# fruits[0] -> error
#세트에 들어가는 요소는 중복될 수 없으며, 중복될 경우 한 개만 포함됨.

print('02 세트에 특정 값 확인')
print('orange' in fruits)

print('03 세트 요소 추가 및 삭제')
a.add(3) #요소 추가
a.remove(3) #요소 삭제

print('04 세트 연산')
a = set(range(1,8))
b = set(range(5,14))
ab = a|b # 합집합
ab2 = set.union(a,b) #합집합을 출력하는 다른 방법
a_b = a&b #교집합
a_b2 = set.intersection #교집합
amb = a-b #차집합
amb2 = set.difference(a,b) #차집합 
axb = a^b #대칭차집합 (겹치지 않는 요소만 출력)
axb2= set.symmetric_difference(a,b)
print(ab,a_b,amb,axb)
# 아래와 같이 할당 연산자로 사용가능
c = set(range(3,11))
c |= {12}
c |= a
c &= a
c -= a
a ^= a
#부분 집합 확인
a = {1,2,3}
b = {1,2,3,4}
print(a < b) #a가 b의 부분집합인가?
print(a <=b) #

