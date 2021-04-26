"""
각자릿수마다 그룹으로 나누어서 품.
트라이 풀이와 비슷한 듯함. [풀 당시에는 트라이 개념을 모름]

아래는 다른 사람의 풀이로 정렬을 이용해 품.
___________________________
숫자가 아닌 문자열 기준으로 할 경우
// 정렬 전
134
15
12
134
1234

// 정렬 후
12
1234
13
134
15
정렬된 숫자를 기준으로 
인덱스 i는 다음 인덱스 i + 1에 대해 포함되었는지만 판단하면 문제를 해결가능
"""


import sys
class Testcase :
  def group(self,numlist):
    groups = [[] for t in range(10)]
    check = [0 for t in range(10)]
    for ele in numlist :
      first = int(ele[0])
      if(check[first]>0):
        self.result = 'NO'
        return 
      elif(len(ele)==1):
        check[first] = 1
      else:
        groups[first].append(ele[1:]) 
    for ele in groups :
      if len(ele)>0:
        self.group(ele)
  def __init__(self):
    N = int(input())
    num_list = []
    self.result ='YES' 
    for t in range(N):
     num_list.append(sys.stdin.readline().rstrip())
    num_list.sort()
    self.group(num_list)
T = int(input())
for t in range(T):
  sol = Testcase()
  print(sol.result)
