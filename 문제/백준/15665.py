#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> v;
vector<int> S;
int visit[8] = {0,};
int N,M;


void combination(int start, int depth)
{
  if(depth==M)
  {
    for(auto ele : v)
        cout<<ele<<" ";
    cout<<endl;
    return;
  }
  for(int i=start;i<N+depth-M+1;i++)
  {
    if(visit[i])
      continue;
    v.push_back(S[i]);
    visit[i] = 1;
    combination(i+1,depth+1);
    v.pop_back();
    visit[i] = 0;
  }
   
}

int main() {
    cin>>N>>M;
    for(int i=0;i<N;i++)
    {
     int temp;
      cin>>temp;
      S.push_back(temp); 
    }
    sort(S.begin(),S.end());
    combination(0,0);
 
}