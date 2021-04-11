#include <iostream>
// vector 헤더를 사용한다.
#include <vector>
using namespace std;
vector<vector<int>> adj;
int main(void)
{

    //1. 2차원 vector 선언은 일반적인 vector와 동일함.
    vector<vector<int>> v;
    // 이렇게 선언된 2차원 vector는 vector<int>를 넣어야 함.
    vector<int> v2;
    v.push_back(v2); //빈 1차원 vector 넣음
    v[0].push_back(1);
    cout<<v[0][0]<<endl; //1 출력
    //초기화는 아래 방법으로 가능
    vector < vector <int> > v(10,vector <int>(10,0));
    //글로벌 변수로 선언한 경우 아래와 같이 초기화 가능.
    int numCourses = 100;
    vector<int> v5;
    adj.assign(numCourses,v5);
}



 
