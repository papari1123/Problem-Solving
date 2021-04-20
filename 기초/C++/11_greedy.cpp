/*
그리디 알고리즘은 아래 조건에 만족해야 적용이 가능함.
- 최적부분구조 : 주어진 문제 P에 대한 최적의 솔루션이 P의 부분 문제들의 최적의
솔루션으로 구성될 경우
- 그리디 선택 : 주어진 문제 P에 대한 지역적 최적 솔루션을 반복적으로 선택하여 전체 최적 솔루션을
구할 수 있을 경우.

대표적으로 아래 문제들이 있음
1. 최단작업 우선 스케줄링
2. 분할 가능 배낭 문제
3. 최소 신장 트리 문제 (MST)
4. 유니온 파인드
*/

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int N;
int wait = 0;
long long result = 0;
vector<int> p;
int main(void)
{
    cin>>N;
    for(int i=0;i<N;i++)
    {
        int temp;
        cin>>temp;
        p.push_back(temp);
    }
    sort(p.begin(),p.end());
    for(int i=0;i<N;i++)
    {
        result += wait;
        wait += p[i];
    }
    result+=wait;
    cout<<result;

    return 0;
}