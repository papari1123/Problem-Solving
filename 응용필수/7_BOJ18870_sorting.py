"""
더 좋은 풀이는 딕셔너리를 이용:
# 리스트 안 중복을 제거하고 오름차순으로 정렬
xt = list(sorted(set(x)))

# 작은 것부터 차례대로 원래 값을 key, 압축된 좌표를 value로 딕셔너리에 저장
xt = {xt[i]: i for i in range(len(xt))}

# 원래 리스트의 값을 딕셔너리 key로 넣어서 value를 출력
# 이때 *을 붙이면 띄어쓰기 형식으로, 안 붙이면 리스트로 출력됨
print(*[xt[i] for i in x])
"""

import sys
N = int(input())
X = list()
X = list(map(int,sys.stdin.readline().rstrip().split(" ")))
Y = [[X[i],i] for i in range(N)]
Z = sorted(Y, key=lambda x: x[0])
cnt = 0 #init
last = Z[0][0]
for ele in Z:
  if(last<ele[0]):
    cnt += 1
    last = ele[0]
  ele[0] = cnt
Result = sorted(Z, key=lambda x: x[1])
for i in Result :
  print(i[0],end=' ')