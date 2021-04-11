/*
동적할당 기본문제
* list 만들 시 가급적 인덱스 1부터 시작할 것.
->크기 N이랑 같이 쓸 때 혼동됨.
*/


#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>
using namespace std;
const int UNKNOWN = -1;
int N;
int p[1001][3];
int dp_[1001][3];


int DP(int n, int color)
{
    if(dp_[n][color] != UNKNOWN)
    {
        return dp_[n][color];
    } 
    if(n>1)
    {
        switch(color)
        {
            case 0:
                dp_[n][color] = min(DP(n-1,1),DP(n-1,2))+p[n][0];
                break;
            case 1:
                dp_[n][color] = min(DP(n-1,0),DP(n-1,2))+p[n][1];
                break;     
            case 2:
                dp_[n][color] = min(DP(n-1,0),DP(n-1,1))+p[n][2];     
                break;
        }
    }
    else
    {
        dp_[n][color] = p[1][color];
    }
    return dp_[n][color];

}

int main(void)
{
    cin>>N;
    for(int i=1;i<=N;i++)
    {
        for(int j=0;j<3;j++)        
        {
            cin>>p[i][j];
            dp_[i][j] = UNKNOWN;
            
        }
    }

    cout<<min(min(DP(N,0),DP(N,1)),DP(N,2));

    return 0;
}