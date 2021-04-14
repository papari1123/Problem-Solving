/*
공식으로 구할 수도 있음

여기서는 재귀를 이용해서 품.
**그냥 카운팅하면 O(2^N)이라 시간 초과나서, skip 과정 필요.

*/

#include <iostream>
#include <vector>
#include <math.h>
using namespace std;
int N,r,c;
int num = 0;
int result = -1;
pair<int,int> add[] = {{0,0},{1,0},{0,1},{1,1}};
void z(int size,int x,int y)
{
    if(result>=0)
        return;
    if(c<x||c>=x+size||r<y||r>=y+size)
    {
        num += size*size;
        return;
    }
       
   // cout<<"s"<<size<<" "<<x<<" "<<y;
    if(size==2)
    {
        for(int i=0;i<4;i++)
        {
            if(c==(x+add[i].first)&&r==(y+add[i].second))
            {
                result = num;
                return;
            }
           // cout<<x+add[i].first<<","<<y+add[i].second<<" ";
            num++;
        }
    

    }
    else
    {
    z(size/2,x,y);
    z(size/2,x+size/2,y);
    z(size/2,x,y+size/2);
    z(size/2,x+size/2,y+size/2);
    }
}
int main(void)
{
    cin>>N>>r>>c;
    
    z((int)pow(2,N),0,0);
    cout<<num;
    return 0;
}