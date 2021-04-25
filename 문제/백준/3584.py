"""
* LCA 문제
만약 트리의 루트가 어떠한 노드로 고정되어 있다면 dfs를 통해 탐색가능.
그러나, 루트가 정해져있지 않기 때문에 아래에서 위로 올라가는 방식을 이용해야 함.
두 정점의 높이를 같게하고 거기서 하나씩 똑같이 올려 가면서 같은 정점이 나올때까지 while문을 반복.
같은 depth에서 시작했기에 depth를 똑같이 증가시키다 만난 같은 정점이 가장 가까운 공통 조상이 됨.

아래 문제는 괜히 Node class도 만들고 dictionary 써서 복잡하지만, 문제만 풀자면 간단함.
일단 엣지 정보를 2차원 list[[N-1]X2]에 저장한 후, 
공통조상을 찾을 노드의 parent list를 만든 후, 가장 depth가 낮게 형성된
공통 조상을 출력하면 됨. 
"""

import sys
class Node:
    def __init__(self, value, childIndexList, parentIndex):
        self.value = value
        self.child = childIndexList
        self.parent = parentIndex

class TestCase:
    def findCommonParent(self,a,b):
      parentA = [a]
      parentB = [b]
      while(self.nodeDic[parentA[-1]].parent is not None):
          parentA.append(self.nodeDic[parentA[-1]].parent)
      while(self.nodeDic[parentB[-1]].parent is not None):
          parentB.append(self.nodeDic[parentB[-1]].parent)
      for ele in parentA:
        if(ele in parentB):
          print(ele)
          return



    def __init__(self):
        self.nodeDic = {} #노드 중복 생성 방지
        self.N = int(sys.stdin.readline().rstrip())
        for t in range(self.N-1):
            parent, child = map(int,sys.stdin.readline().rstrip().split())
            if(child not in self.nodeDic):
                node = Node(child,[],parent)
                self.nodeDic.update({child:node})
            else:
                self.nodeDic[child].parent = parent    
            if(parent not in self.nodeDic):
                node = Node(parent,[child],None)
                self.nodeDic.update({parent:node})
            else:
                self.nodeDic[parent].child.append(child)
        
T = int(sys.stdin.readline().rstrip())
for t in range(T):
    sol = TestCase()
    a,b = map(int,sys.stdin.readline().rstrip().split())
    sol.findCommonParent(a,b)
    # TEST 목적
    #for ele in sol.nodeDic.values():
    #    print("node:",ele.value)
    #    print("parent:",ele.parent)
    #    for ele2 in ele.child:
    #      print("child:",ele2)