# 이터레이터(iterator)는 값을 차례대로 꺼낼 수 있는 객체(object).
# for i in range(100):은 0부터 99까지 연속된 숫자를 만들어낸다고 했는데,

# 사실은 숫자를 모두 만들어 내는 것이 아니라 0부터 99까지 값을 차례대로 꺼낼 수 있는 
# 이터레이터를 하나만 만들어냄. 

# 이후 반복할 때마다 이터레이터에서 숫자를 하나씩 꺼내서 반복.
# 만약 연속된 숫자를 미리 만들면 숫자가 적을 때는 상관없지만 숫자가 아주 많을 때는 메모리를 많이 사용하게 됨.

# 그래서 파이썬에서는 이터레이터만 생성하고 값이 필요한 시점이 되었을 때 값을 만드는 방식을 사용. 
# 즉, 데이터 생성을 뒤로 미루는 것인데 이런 방식을 지연 평가(lazy evaluation)라고 함.


#1. iterable한지 알아보기
print(dir([1,2,3]))
# dir 함수를 이용해 객체의 메서드를 확인할 수 있음. -> __iter__ 메서드가 있는지 확인.

#2. iterator를 가져오기
it = [1,2,3].__iter__()
print(it.__next__()) # __next__하면 차례대로 요소를 꺼낼 수 있다.
print(it.__next__())
print(it.__next__())
try:
    print(it.__next__()) # 꺼낼 요소가 없으면 StopIteration 예외를 발생시킨다.
except:
    print('Stop Iteration')

#3. for에서 iterator의 사용
# 반복가능한 객체인 range는 __iter__로 이터레이터를 얻고 __next__를 반복함.
# __iter__, __next__를 가진 객체를 이터레이터 프로토콜을 지원한다고 할 수 있음.
for i in range(3): 
    print(i)

#4. iterator 만들기
"""
class 이터레이터이름:
    def __iter__(self):
        코드
    def __next__(self):
        코드
"""
class Counter:
    def __iter__(self, stop):
        self.current = 0
        self.stop = stop
    
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.current < self.stop:
            r = self.current
            self.current += 1
            return r
        else
            raise StopIteration
for i in Counter(3):
    print(i,end=' ')

#5. 이터레이터의 unpacking
a,b,c = Counter(3) # 여러개의 변수에 할당할 수 있다.
print(a,b,c)

#6. 인덱스를 활용한 iterator
# __getitem__을 이용해 인덱스로 접근할 수 있는 이터레이터를 만들 수 있다.
class Counter_index:
    def __init__(self, stop):
        self.stop = stop;
    deof __getitem__(self, index):
        if  index < self.stop :
            return index
        else :
            return IndexError
print(Counter_index(3)[0])