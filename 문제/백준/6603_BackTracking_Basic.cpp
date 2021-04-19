#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
#define MAX_DEPTH 6
vector<int> v;
vector<int> S;
int visit[49] = {0,};
int k;


void combination(int start, int depth)
{
  if(depth==MAX_DEPTH)
  {
    for(auto ele : v)
        cout<<ele<<" ";
    cout<<endl;
    return;
  }
  for(int i=start;i<k+depth-MAX_DEPTH+1;i++)
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
  while(1)
  {
    cin>>k;
    if(k==0)
      break;
    for(int i=0;i<k;i++)
    {
     int temp;
      cin>>temp;
      S.push_back(temp); 
    }
    sort(S.begin(),S.end());
    combination(0,0);
    // clear
    for(int i=0;i<k;i++)
      S.pop_back();
    cout<<endl;
  }
  
}
