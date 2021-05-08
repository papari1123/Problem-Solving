# 람다 표현식 = 익명 함수
# 매개변수, 연산자, 값 등을 조합한 식으로 반환값을 만드는 방식.
def add_one(x):
  return x + 1
print(add_one(1)) #일반적인 함수를 이용하는 방법
add_one_lambda = lambda x:x + 1 # 이 lambda 함수는 x를 입력으로 받고 x+1을 출력으로 받는다.
print(add_one_lambda(1))
print((lambda x:x+1)(1)) # 람다 표현식을 ()로 묶어 바로 호출이 가능함.
# 1. 람다 표현식 안에는 새 변수를 만들 수 없음
# 2. 반환값 부분에 변수없이 식 한줄로 표현해야 함.:
# (lambda x:y=1;x+y)(1) -> invalid syntax
# 3. 외부 변수는 사용할 수 있음
y = 1 
print((lambda x:x+y)(1))
# 4. 람다 함수를 다른 함수의 인수로 넣기 (map 객체 활용)
print(list(map(lambda x:x+2,[1,2,3,4])))

# 5. 람다 표현식에 조건부 표현식 사용하기
# lambda 매개변수들: 식1 if 조건식 else 식2
# 모든 경우에 대한 반환값을 알기 위해, 반드시 else 구문을 넣어야 함.
a = [1,2,3,4,5,6,7,8,9]
print(list(map(lambda x : str(x) if x %4 == 0 else x, a)))

# 6. map에 객체 여러 개 넣기
a = [1,2,3,4,5]
b = [2,4,6,8,10]
print(list(map(lambda x,y:x*y,a,b)))

# 7. filter 사용하기
# filter는 반복가능한 객체에서, 지정한 함수의 반환값이 true일 때 해당 요소를 가져옴.
a = [1,2,3,4,5,6,7,8,9]
print(list(filter(lambda x: x>6 or x<3, a)))

# 8. reduce 사용하기
# reduce는 반복가능한 객체에 대해 각 요소를 지정한 함수로 처리하여, 이전 결과가 누적되어 반환되는 함수임.
from functools import reduce
print(reduce((lambda x,y:x+y),a))
