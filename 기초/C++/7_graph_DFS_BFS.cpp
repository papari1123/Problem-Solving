#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

///**1. 무방향 그래프일 경우 대칭행렬
//**2. 엣지 정렬 *작은순부터 탐색하려면 매우 중요함.
//**3. 대부분의 문제가 노드 인덱스를 1부터 하므로 이에 주의함.
int v;
vector<vector<int>> graph;
int e;
int start;
vector<int> check;
queue<int> q;
void BFS(int start)
{
    
    check[start] = 1;
    q.push(start);
    while(!q.empty())
    {
        int index = q.front();
        cout<<index<<" "; // out
        q.pop();
        for(int i=0;i<graph[index].size();i++)
        {
            int next = graph[index][i]; 
            if(check[next]==0)
            {
                check[next] = 1;
                q.push(next); 
            } 
        }           
    }
}
void DFS(int index)
{
    check[index] = 1;
    cout<<index<<" ";
    for(int i=0;i<graph[index].size();i++)
    {
        int next = graph[index][i];
        if(check[next]==0)
            DFS(next);
    } 
    //check[index] = 0;
    return;
}

int main(void)
{
    //2. 인접리스트를 이용한 방법.

    // 노드 수,엣지 수, 시작지점  입력
    cin>>v>>e>>start;   
    vector<int> emp;
    graph.assign(v+1,emp); // index 1번부터 하도록 v+1
    check.assign(v+1,0);
    // 엣지입력
    for(int i=0; i<e;i++)
    {
        long a,b,weight;
        cin>>a>>b;
        graph[a].push_back(b); //{,} => makepair 
        graph[b].push_back(a);  //**1. 무방향 그래프일 경우 대칭행렬
       
    }
    
    //**2. 엣지 정렬 *작은순부터 탐색하려면 매우 중요함.
	// 나중에 하나의 정점에서 다음을 탐색할 때 node 값에 순차적으로 접근해야하기 때문
    //**** 1번부터 index하도록 함.
	for(int i=1; i<=v; i++){
		sort(graph[i].begin(), graph[i].end());
	}
    // 값확인
    /*
    for(int i=0;i<v;i++)
    { 
        for(int j=0;j<graph[i].size();j++)
        {
            cout << graph[i][j]<<" "; //col
        }
         cout <<endl;
    }
   */

    DFS(start);
    for(int i = 0; i<check.size();i++) //DFS에 의한 체크리스트 삭제
     check[i] = 0;
    cout<<endl;
    BFS(start);
    return 0;
}
