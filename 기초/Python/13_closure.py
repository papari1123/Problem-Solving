# 1. 전역 변수와 지역 변수
# 함수 내에서 변수를 선언할 경우 지역변수가 되며, 
# 함수 외부에서 선언한 전역 변수와 별개로 취급된다.
x = 10          # 전역 변수
def foo():
    x = 20      # x는 foo의 지역 변수
    print(x)    # foo의 지역 변수 출력
 
foo()
print(x)        # 전역 변수 출력

# 2. global과 local
# 함수 안에서 global을 사용하면 전역변수를 사용할 수 있음
# local()은 해당 네임스페이스를 딕셔너리 형태로 출력함.
y = 1
def fool():
  global y
  x = 5
  print(x)
  print(y)
  print(locals())
fool()

# 3. closure
# 함수를 둘러싼 환경(지역 변수, 코드 등)을 계속 유지하다가, 
# 함수를 호출할 때 다시 꺼내서 사용하는 함수를 클로저(closure)라고 함.
# 여기서는 c에 저장된 함수가 클로저임.

def calc():
    a = 3
    b = 5
    def mul_add(x):
        return a * x + b    # 함수 바깥쪽에 있는 지역 변수 a, b를 사용하여 계산
    return mul_add          # mul_add 함수를 반환
 
c = calc() # closure
print(c(1), c(2), c(3), c(4), c(5))
