/*STACK 사용해 구현, 근데 QUEUE방식이 나을 듯 하다.*/

#include <iostream>
#include <vector>
#include <stack>
using namespace std;
int T;
int M,N,K;
int axis[52][52]; // 0= no, 1== yes, 2 == visited
stack<pair<int,int>> s;
int check()
{
    int cnt = 0;
    for(int i=0;i<M;i++)
    {
        for(int j=0;j<N;j++)
        {
            if(axis[i][j]==1)
            {
              
                int a,b;
                cnt++;
                a = i;
                b = j;
                while(1)
                {
                    axis[a][b] = 2;
                    if(a<M && axis[a+1][b]==1)
                    {
                        a++;
                        s.push({1,0});
                    }
                    else if(a>0 && axis[a-1][b]==1)
                    {
                        a--;
                        s.push({-1,0});
                    }
                    else if(b>0 && axis[a][b-1]==1)
                    {
                        b--;
                        s.push({0,-1});
                    }
                    else if(b<N && axis[a][b+1]==1)
                    {
                        b++;
                        s.push({0,1});
                    }
                    else if(a!=i || b!=j)
                    {
                        a -= s.top().first;
                        b -= s.top().second;
                        s.pop();
                    }
                    else 
                        break;
                }
            }
        }
    }
    return cnt;
}
int main(void)
{
    cin>>T;
    for(int i=0;i<T;i++)
    {
        cin>>M>>N>>K;
        for(int j=0;j<K;j++)
        {
            int x,y;
            cin>>x>>y;
            axis[x][y]=1;
        }
        cout<<check()<<endl;
    }


    return 0;
}