#include <iostream>
#include <vector>
using namespace std;

pair<int,int> pair_[41];
int T;

pair<int,int> getResult(int n)
{
    if(pair_[n].first!= -1)
        return pair_[n];
    pair_[n] = {getResult(n-1).first+getResult(n-2).first,getResult(n-1).second+getResult(n-2).second};
    return pair_[n];
  
}
int main(void)
{
    cin>>T;
    for(int i=0;i<41;i++)
        pair_[i] = {-1,0};
    pair_[0] = {1,0};
    pair_[1] = {0,1};
    for(int i=0;i<T;i++)
    {
       int n;
       cin>> n;
       pair<int,int> result = getResult(n);
       cout<<result.first<<" "<<result.second<<endl;

     }
     return 0;
}