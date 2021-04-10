#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;
bool compare(string a, string b)
{
   if(a.length()==b.length())
   {
       return a<b;
   }
   else
   {
       return a.length()<b.length();
   }
}
int main(void)
{ 
    int n;
    cin>>n;
    vector<string> s;
   
    for(int i =0; i<n;i++)
    {
        string temp;
        cin>>temp;   
        s.push_back(temp);
    }
    sort(s.begin(),s.end(),compare); // compare함수에 의해 정렬.
    s.erase(unique(s.begin(),s.end()), s.end()); // 중복값 제거.
    for(auto ele : s)
        cout<<ele<<endl;  
    return 0;
}
