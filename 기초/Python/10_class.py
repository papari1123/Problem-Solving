"""
Class 내의 함수를 메소드라고 함.
메소드의 매개변수는 무조건 self가 포함되어야 함.
"""
class Person:
    def __init__(self):
        self.hello = '안녕하세요.' #속성값
    def greeting(self):  
        print(self.hello)
    def printVariable(self,pro,*listComponent): #가변인자 다루기
        print(pro)
        print(listComponent)

me = Person()
me.greeting() 
me.printVariable('test','apple','banana','kiwi')