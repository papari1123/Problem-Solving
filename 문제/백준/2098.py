min_cost = 999999999
cost = 0
N = int(input())
W = [list(map(int,input().split(' '))) for i in range(N)]
S = []
visit = [0 for i in range(N)]
def DFS(index,depth):
    global cost,min_cost,N,W,S,visit
    for i in range(N):
        v = W[index][i]  
        if(i==0 and v>0 and len(S)==N) :
            min_cost = min([cost+v,min_cost])
        elif (v>0 and visit[i] == 0 and cost+v<min_cost):
           visit[i] = 1
           S.append(v)
           cost += S[-1]
           DFS(i,depth+1)
    visit[index] = 0
    cost -= S[-1]
    S.pop()
visit[0] = 1
S.append(0)
DFS(0,0)
print(min_cost)