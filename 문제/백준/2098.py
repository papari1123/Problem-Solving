## global 변수에 빠진 변수가 없는지 주의. -> 더좋은 방법은 없나?
## DES함수의 현재 노드 위치(index)와 상태(visit)를 저장한 메모지에이션 방식을 사용하지


def DFS(index,visit):
    global N,W,cost, DP_min_cost
    if(DP_min_cost[index][visit]!=-1):
       return DP_min_cost[index][visit]      
    if(visit==(1<<N)-1 and W[index][0]>0): # 모든 노드를 돌고, 첫노드로 회귀가능한 경우
        return W[index][0]
    DP_min_cost[index][visit] = 999999999 # 초기화
    for i,v in enumerate(W[index]) :
        if visit&(1<<i)==0 and v>0:
            DP_min_cost[index][visit] = min(v+DFS(i,visit| (1<<i)),DP_min_cost[index][visit])
    return  DP_min_cost[index][visit]       

N = int(input()) 
W = [list(map(int,input().split(' '))) for x in range(N)]
cost = 0 #현재 cost
DP_min_cost = [[-1 for i in range(1<<16)] for j in range(N)] # 남은 경로에 대한 최소 cost  
print(DFS(0,(1<<0))) # 코스트 반환하는 DFS
