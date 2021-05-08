# 람다 표현식 = 익명 함수
# 매개변수, 연산자, 값 등을 조합한 식으로 반환값을 만드는 방식.
def add_one(x):
  return x + 1
print(add_one(1)) #일반적인 함수를 이용하는 방법
add_one_lambda = lambda x:x + 1 # 이 lambda 함수는 x를 입력으로 받고 x+1을 출력으로 받는다.
print(add_one_lambda(1))
print((lambda x:x+1)(1)) # 람다 표현식을 ()로 묶어 바로 호출이 가능함.
# 1. 람다 표현식 안에는 새 변수를 만들 수 없음
# 2. 반환값 부분에 변수없이 식 한줄로 표현해야 함.
try:
  (lambda x:y=1;x+y)(1) 
except:
  print('error')
# 3. 외부 변수는 사용할 수 있음
y = 1 
print((lambda x:x+y)(1))
# 4. 람다 함수를 다른 함수의 인수로 넣기 (map 객체 활용)
print(list(map(lambda x:x+2,[1,2,3,4]))
