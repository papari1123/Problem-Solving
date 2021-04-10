#include <bits/stdc++.h>

using namespace std;
int main(void)
{
    //STACK
    //1. 선언의 기본은 stack<datatype> 변수이름;
    stack<int> s;
    //2. stack 멤버변수
    /*
    s.size() : s의 사이즈
    s.empty() : s의 사이즈가 0인지 확인.
    s.top() : s에서 가장 나중에 들어간 원소 리턴.
    s.push(var) : s의 맨 뒤에 var를 추가.
    s.pop() : s의 가장 나중에 들어간 원소를 삭제
    */
   for(int i = 0;i<=10; i++)
       s.push(i);
   while(!s.empty())
   {
       int n = s.top();
     
       cout<<n<<" "<<s.top()<<endl;
    s.pop();
   }
   // QUEUE
    //1. 선언의 기본은 queue<datatype> 변수이름;
    queue<int> q;
    //2. queue 멤버변수
    /*
    q.size() : q 사이즈
    q.empty() : q 사이즈가 0인지 확인.
    q.front() : q에서 제일 앞에 있는 변수 반환. (가장 나중에 들어간)
    q.back() : q에서 제일 뒤에 있는 변수 반환.
    q.push(var) : q의 맨 뒤에 var를 추가.
    q.pop() : q의 가장 나중에 들어간 원소를 삭제
    */
    cout<<"queue:"<<endl;
    for(int i = 0;i<=10; i++)
       q.push(i);
   while(!q.empty())
   {
       int n = q.front();
       q.pop();
       cout<<n<<" "<<q.back()<<endl;

   }
   return 0;
}


