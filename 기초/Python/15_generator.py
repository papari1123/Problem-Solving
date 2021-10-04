"""
- 제너레이터는 이터레이터를 생성해주는 함수이다.
* 이터레이터(iterator)는 값을 차례대로 꺼낼 수 있는 객체(object).
- 이터레이터는 클래스에 __iter__, __next__ 또는 __getitem__ 메서드를 구현해야 하지만
- 제너레이터는 함수 안에서 yield 키워드만 사용하면 됨.
- 제너레이터는 제너레이터 객체에서 __next__ 메서드를 호출할 때마다 함수 안의 yield까지 코드를 실행하며 yield에서
  값을 발생시킴.
"""
# 1. yield 를 이용해 제너레이터를 만들어보기.
def number_generator():
    yield 0
    yield 1
    yield 2

# yield를 사용하면, *값을 함수 바깥으로 전달하면서 코드 실행을 함수 바깥에 양보함.
# yield는 현재 함수를 잠시 중단하고 함수 바깥의 코드가 실행되도록 만듦.


for i in number_generator():
    print(i)

it = number_generator()
print(next(it)) # yield가 호출되어 값을 함수 바깥으로 리턴함.
print(next(it))
print(next(it))


# 2. 제너레이터에서 return 사용
# 제너레이터에서 return 사용하면 StopIteration exception이 발생하고, 이에 따른 error값은 return 값이 된다.
def one_generator():
  yield 1
  return 'err_value'

try:
   g = one_generator()
   next(g)
   next(g)
except StopIteration as e:
   print(e) 

# 3. 제너레이터 응용 1
# yield를 활용하면 좀 더 쉽게 이터레이터를 만들 수 있음.
# 아래와 같이 range(횟수)와 같은 제너레이터를 만들 수 있다.
def counter_generator(stop):
  n = 0
  while n < stop:
    yield n
    n += 1 

cnt_g = counter_generator(5)

for i in cnt_g  :
   print(i)

# 4. yield에서 함수 호출
def upper_generator(x):
  for i in x:
    yield i.upper() # 함수를 호출할 경우에도 해당 함수의 반환값을 바깥으로 전달함.
word = ['end','start','middle'] 
for i in upper_generator(word):
  print(i)


# 5. yield from을 사용
print('use yield from')
# 5.1 yield from 반복가능한 객체
def number_from_generator():
    x = [1,2,3]
    yield from x

for i in number_from_generator():
    print(i)

# 5.2 yield from 이터레이터
def number_iter_generator():
    x = iter([1,2,3])
    yield from (x+2)
    

for i in number_iter_generator():
    print(i)

# 5.3 yield from 제너레이터 객체
def number_gene_geneerator():
    yield from counter_generator(3)

for i in number_gene_geneerator():
    print(i)
