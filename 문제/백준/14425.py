Result = 0
N,M = map(int,input().split(" "))
S = set()

#Set을 이용한 계산
for t in range(N) :
    S.add(input())
for t in range(M) :
    if input() in S :
        Result += 1

print(Result)