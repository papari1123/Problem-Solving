"""
"""
def swap_(a,b):
    z=a
    a=b
    b=z
    return a,b
print('01 함수 사용')
a,b = swap_(1,2)
print(a,b)