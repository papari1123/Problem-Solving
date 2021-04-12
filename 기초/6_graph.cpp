#include <iostream>
#include <vector>
//#define MATRIX
using namespace std;
int main(void)
{
    //1. 인접행렬을 이용한 방법.
    #ifdef MATRIX
    int v = 3;
    long matrix[v][v];
    int e;
    // 엣지 수 입력
    cout << "set edge number : ";
    cin >> e;
    // 초기화
    for(int i=0;i<v;i++)
    { 
        for(int j=0;j<v;j++)
        {
            matrix[i][j] = -1;
        }
    }
    // 엣지입력
    for(int i=0; i<e;i++)
    {
        int a,b,weight;
        cout<<"set edge a b weight";
        cin>>a>>b>>weight;
        if(a>=v || b>=v)
            cout<<"wrong input";
        matrix[a][b] = weight;
    }
    // 값확인
    for(int i=0;i<v;i++)
    { 
        for(int j=0;j<v;j++)
        {
            cout << matrix[i][j]<<" ";
        }
         cout <<endl;
    }
    #else 
    //2. 인접리스트를 이용한 방법.
    int v= 3;
    vector<pair<long,long>> graph[v];
    int e;
    // 엣지 수 입력
    cout << "set edge number : ";
    cin >> e;   
    // 엣지입력
    for(int i=0; i<e;i++)
    {
        long a,b,weight;
        cout<<"set edge a b weight";
        cin>>a>>b>>weight;
        if(a>=v || b>=v)
            cout<<"wrong input";
        graph[a].push_back({b,weight}); //{,} => makepair
    }
    // 값확인
    for(int i=0;i<v;i++)
    { 
        cout <<i<<endl;  //row
        for(int j=0;j<graph[i].size();j++)
        {
            cout << graph[i][j].first<<"("<<graph[i][j].second<<")"<<" "; //col
        }
         cout <<endl;
    }
    #endif
    return 0;
}
