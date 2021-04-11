#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

///**1. 무방향 그래프일 경우 대칭행렬
//**2. 엣지 정렬 *작은순부터 탐색하려면 매우 중요함.

int v= 5;
vector<vector<int>> graph(v);
int e;
int start = 2;
vector<int> check(v);
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

    // 엣지 수 입력
    cout << "set edge number : ";
    cin >> e;   
    // 엣지입력
    for(int i=0; i<e;i++)
    {
        long a,b,weight;
        while(1)
        {  
            cout<<"set edge a b ";
            cin>>a>>b;
            if(a<v && b<v)
                break;
            cout<<"wrong input"<<endl;
        }
        graph[a].push_back(b); //{,} => makepair 
        graph[b].push_back(a);  //**1. 무방향 그래프일 경우 대칭행렬
    }
    //**2. 엣지 정렬 *작은순부터 탐색하려면 매우 중요함.
	// 나중에 하나의 정점에서 다음을 탐색할 때 node 값에 순차적으로 접근해야하기 때문
	for(int i=0; i<v; i++){
		sort(graph[i].begin(), graph[i].end());
	}
    // 값확인
    for(int i=0;i<v;i++)
    { 
        for(int j=0;j<graph[i].size();j++)
        {
            cout << graph[i][j]<<" "; //col
        }
         cout <<endl;
    }
   

    cout<<"BFS :";
    BFS(start);
    for(int i = 0; i<check.size();i++) //BFS에 의한 체크리스트 삭제
     check[i] = 0;
    cout<<"\nDFS :";
    DFS(start);
    
   
    return 0;
}
