"""
https://programmers.co.kr/learn/courses/30/lessons/43164
"""


"""
내가 푼 풀이

1.  default dict 사용안함
2. tickets에서 값 펼칠 때  for i,j in tickets: 와 같이 펼칠 수 있음

def solution(tickets):
    tickets = sorted(tickets, key = lambda x : (x[0],x[1]))
    airports = {}  # (next_port, visit)
    visit = []
    for t in tickets:
        if t[0] in airports:
            airports[t[0]].append([t[1],0])
        else:
            airports[t[0]] = [[t[1],0]]
   
    def dfs(curr_port):

        if(len(visit)==len(tickets)+1):
            return True
        if(curr_port not in airports):
            return False
        print(airports)
        for idx, next_port in enumerate(airports[curr_port]):
            if (next_port[1] == 0):
                visit.append(next_port[0])
                next_port[1] = 1
                if(dfs(next_port[0])):
                    return True
                next_port[1] = 0
                visit.pop()
        return False 
    visit.append('ICN')
    dfs('ICN')        
    return visit
"""