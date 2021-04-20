#include<iostream>
#include <algorithm> // sort를 위해 필요

vector<int> v;
vector<string> s;
bool compare(int,int);

int main(void)
{
    // 1. 오름차 순 (default)
    sort(v.begin(), v.end());
    sort(v.begin(), v.end(), greater<int>());   
    // 2. 내림차 순
    sort(v.begin(), v.end());
    // 3. 사용자 정의
    // 주의해야 할 점은 인자로는 compare()가 아닌 compare를 넣어줘야 한다는 것이다.
    // compare의 반환값은 bool임.
    sort(s.begin(), setlocale.end(), compare);            //사용자 정의 함수 사용

    // 4. 중복된 값을 제거하려면 sort 후, unique,ereae.
    // unique는 중복되는 값들은 v.end()뒤쪽으로 다 빼는 역할을 함.
    /*v.erase(v.begin()+s, v.begin()+e) 명령어를 입력하면 [s,e) 원소가 삭제된다.
     즉 시작 지점은 닫힌구간, 끝나는 지점은 열린 구간으로 삭제된다.*/

    //sort(v.begin(), v.end()); 앞에서 sorting해줬으면 상관없음.
    s.erase(unique(s).begin(),s.end()), s.end());
}


  /* 아래와 같을 경우 문자열 길이가 같으면 사전순, 다르면 길어지는 순으로 정렬됨.  */
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

    

