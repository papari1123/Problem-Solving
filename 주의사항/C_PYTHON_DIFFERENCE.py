"""
1. C/C++은 call by referece 또는 call by assignment지만,
Python은 call by assignment이다.

Python에서는 모든 것이 객체(심지어 상수도)이며, 따라서  
아래 combination solution에서
 output.append(curr[:])를 보면,

"""
li1 = []
li2 = []
li3 = []
ele = [1]
# 상수는 immutable이라 C언어처럼 사용가능
for i in range(5):
    li1.append(i)
# ele가 list 객체이기 때문에, li2에 들어가는 것은 ele 객체 자체이며 call by referece 개념과 유사함.
for i in range(5):
    li2.append(ele)
    ele[-1] += 1
# ele[:]는 list 객체 안의 element를 복사해 반환하므로 call by assignment 개념과 유사함.
for i in range(5):
    li3.append(ele[:])
    ele[-1] += 1
print(li1,li2,li3)
