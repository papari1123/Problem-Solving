import copy
print('01. 리스트 동적 생성')
a = [] # 빈 리스트 생성
a.append([]) # 빈리스트에 첫번째 요소를 빈리스트로 생성
a[0].append(10) # a[0][0]에 10 할당
a[0].append(20)

print('02. for을 이용한 리스트 요소 확인')
a = [[1,2],
     [3,4],
     [5,6]]
for x,y in a:
    print(x,y)

print('03. for과 range를 이용한 출력')
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end = ' ')
    print()

print('04. 리스트 표현식을 이용한 2차원 리스트 출력')
a = [[0 for j in range(5)] for i in range(3)]
b = [[0] * 5 for i in range(3)]
print(a)
print(b)

print('05. 다차원 리스트 복사')
a = [[0,1],[1,2]]
b = a
c = a.copy()
d = copy.deepcopy(a) #깊은 복사, import copy 필요
a[0][0] = 99
b[0][1] = 9
c[1][0] = 4
print(a)
print(b)
print(c)
print(d)



