import time
"""
 DP는 분할정복을 확장한 문제로, 같은 부분 문제가 반복적으로 나타남.
 기본적으로 아래 두가지 조건을 만족함.
  1. 중복되는 부분 문제 특성으로 인해 문제의 복잡도가 입력이 증가함에 따라 기하급수적으로 늘어나나,
     최적 부분 구조 속성을 활용해 복잡도를 줄임.
  2. 반복 계산을 피하기 위해 이전 해결한 부분 문제의 해답을 캐시에 저장함.
  : 이를 위해, 백트레킹, 메모이제이션, 타뷸레이션 등이 활용될 수 있음. 
"""
# 팩토리얼 문제을 보통의 재귀로 풀경우.
def Fibonacci(n):
    if n<2:
        return n
    return Fibonacci(n-1)+Fibonacci(n-2)

# 메모이제이션을 쓰는 경우. (하향식 접근법)
f = [-1]*100 
def Fibonacci_memoization(n):
    if n<2:
        return n
    if f[n]!=-1:
        return f[n]
 
    f[n] = Fibonacci_memoization(n-1)+Fibonacci_memoization(n-2)
    return f[n]

# 타뷸레이션을 쓰는 경우 (상향식 접근법)
# - 메모리 사용량이 효율적이며, 가능한 모든 상태를 기록하는 룩업테이블 생성가능.
# - 주어진 문제에 대해 임의의 여러 상태를 참조해야 하는 경우 최적.

dp = [0]
def Fibonacci_tabulation(n):
    dp.append(1) #dp[1]
    dp.append(1) #dp[2]
    for i in range(3,n+1):
        dp.append(dp[i-1]+dp[i-2])
    return dp[n]

N = int(input('input n : '))
"""
s= time.time()*1000
ans = Fibonacci(N)
e = time.time()*1000
print("normal recursion: ",ans,e-s,"ms")
"""
s = time.time()*1000
ans = Fibonacci_memoization(N)
e = time.time()*1000
print("memoization: ",ans,e-s,"ms")
s = time.time()*1000
ans = Fibonacci_tabulation(N)
e = time.time()*1000
print("tabulation: ",ans,e-s,"ms")
