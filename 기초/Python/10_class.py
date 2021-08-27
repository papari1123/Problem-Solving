"""
Class 내의 함수를 메소드라고 함.
메소드의 매개변수는 무조건 self가 포함되어야 함.
"""

"""
Method 정의
- 멤버함수라고도 하여 해당 클래스의 object로만 호출 가능
- method는 객체 레벨에서 호출되어, 해당 객체 속성에 대한 연산을 행함.
- {obj}.{method}() 형태로 호출 

Method type
- instance method - 객체로 호출
: 메소드는 객체 레벨로 호출되므로 해당 메소드를 호출한 객체에만 영향.
- class method - class로 호출
: 클래스 메소드의 경우, 클래스 레벨로 호출되므로 클래스 멤버 변수만 변경 가능
ex) staticmethod
"""

class Person:
    def __init__(self, name):
        """
        - 생성자, 클래스 인스턴스가 생성될 때 호출
        - self 인자는 항상 첫 번째에 오며 자기 자신을 가리킴.
        - 이름이 self일 필요는 없지만 일반적으로 self를 사용함.

        - 생성자에서는 해당 클레스가 다루는 데이터를 정의함.
        : 이 데이터를 member variable 또는 attribute라고 함.
        """
        self.hello = name+' 안녕하세요.' #속성값
        """
        self
        - 파이썬의 method는 항상 첫 번째 인자로 self를 전달
        - self는 현재 해당 method가 호출되는 객체 자신을 가리킴
        - java에서의 this와 동일.
        - 이름이 self일 필요는 없으나 위치는 항상 맨 처음의 parameter임.
        """


    def greeting(self):  
        print(self.hello)
    @staticmethod
    def meaning():
        print('인간은 만물의 영장이다.')
    def printVariable(self,pro,*listComponent): #가변인자 다루기
        print(pro)
        print(listComponent)

Person.meaning()
me = Person('펄펄이')
me.greeting() 
me.printVariable('test','apple','banana','kiwi')
you = Person('팔팔이')
you.greeting()


