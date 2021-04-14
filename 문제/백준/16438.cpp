/*
 - N<99, 2^7>=99 이므로
 - 정석은 분할정복으로 풀면 된다.
 - 간단히는 2진수로 나타냈을 때 각 비트값이 팀을 결정하게 하면 됨.
 - 팀에 최소 한 마리 이상의 원숭이가 있어야 하므로 예외처리가 필요하긴 함.


*/

#include <iostream>
#include <vector>
#include <math.h>
using namespace std;
int N;
vector<char> team[7];
char temp;
int main(void)
{
    cin>>N;
    int cnt = 0;
    for(int i=0; i<7 ;i++)
    {
        if((int)pow(2,i)<N)
        {
            for(int j=0; j<N ;j++)
            { 
                cnt++;
                if(cnt>=(int)pow(2,i))
                 {
                     cnt = 0;
                     temp = (temp=='A') ? 'B' : 'A';
                 }
                team[i].push_back(temp);
            } 
        }
        else
        {
             team[i] =  team[i-1]; //dummy5
        }
    
     for(int j=0; j<N ;j++)
     {
        cout<<team[i][j];
     }
     cout<<endl;
    }
    return 0;
}