/*
문제 : https://leetcode.com/problems/course-schedule/
요약 : 그래프에 회귀 경로가 있는지를 검사하는 문제이다.
분류 : graph, DFS, BFS
중요 포인트 :
1. 방향 그래프로 구현해야 하는 문제
2. 회귀 경로가 없어야 하기 때문에 bitmap(check_temp)으로 지나간 경로를 체크하여 검사한다. 
3. 회귀 경로가 없다고 검증이 이미 된 노드에 대해서는 다시 지나칠 필요가 없으므로 또다른 bitmap(visit)를 추가한다.
*/

#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
using namespace std;
int v;
int e;


vector<vector<int>> adj;
vector<bool> visit;
vector<bool> check_temp;
stack<int> s;
 bool flag = true;
    void DFS(int index)
    {
      cout<<index<<" ";
      s.push(index);
      check_temp[index] = true;
      for(int i=0;i<adj[index].size();i++)
      {
          int next = adj[index][i];
         if(visit[next])
             continue;
         else if(!check_temp[next])
             DFS(next);
         else
         {
             flag = false;
             return;
         }
      }
      visit[index] = true;
      s.pop();
    }
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<int> v;
        adj.assign(numCourses,v);
        visit.assign(numCourses,0);
        check_temp.assign(numCourses,0);
        for(int i=0;i<prerequisites.size();i++)
        {
            int highcourse = prerequisites[i][0];
            int lowcourse  = prerequisites[i][1];
            adj[lowcourse].push_back(highcourse);
        }
        for(int i=0; i<numCourses; i++){
		sort(adj[i].begin(), adj[i].end());
	    }
        for(int i=0;i<numCourses;i++)
        {
            if(visit[i]==false)
                DFS(i);
            
        }
        return flag;
    }


int main(void)
{
    vector<vector<int>> in = {{1,0},{2,0},{3,1},{3,2}};
   cout<<endl<<canFinish(5,in);

    return 0;
}