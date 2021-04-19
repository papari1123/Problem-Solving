print('01_for와 range')
for i in range(10): # 0~9
    print('i1:'+ str(i)) 
for i in range(10, 0,-1) : # 10~1, -1씩 감소
    print('i2:' + str(i)) 
for i in reversed(range(10)): # 9~0
    print('i3:'+str(i))
a = [1,2,3,4,5,6,7,8]
for i in a:  # 시퀀스 객체를 넣을 수 있음.
  print('i4:'+str(i))