#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int cnt_b=0;
int cnt_w=0;
int N;
int calRect(bool adj[][128],int n,int i,int j)
{
    int temp[4];
    if(n>=2)
    {
        temp[0] = calRect(adj,n/2,i,j);
        temp[1] = calRect(adj,n/2,i+n/2,j);
        temp[2] = calRect(adj,n/2,i,j+n/2);
        temp[3] = calRect(adj,n/2,i+n/2,j+n/2);
        if(temp[0]!=-1&&temp[1]==temp[2]&&temp[2]==temp[3]&&temp[0]==temp[1])
        {
            return temp[0];
        }
        else
        {
            for(int i=0;i<4;i++)
            {
               if(temp[i]==0)
                    cnt_w++;
                else if(temp[i]==1)
                    cnt_b++;
            }
            return -1;
        }
            
    }
    else
    {
        return adj[i][j];
    }
}
int main(void)
{
    
    bool adj[128][128];
    cin>>N;
    for(int i=0;i<N;i++)
    {
        for(int j=0;j<N;j++)
        {
            cin>>adj[i][j];
        }
    }
    int temp = calRect(adj,N,0,0);
    if(temp==0)
        cnt_w++;
    else if(temp==1)
        cnt_b++;
    cout<<cnt_w<<endl;
    cout<<cnt_b;
    return 0;
}