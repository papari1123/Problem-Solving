#include <iostream>
// vector 헤더를 사용한다.
#include <vector>
using namespace std;
int main(void)
{
    //1. 선언의 기본은 vector<type> 변수이름;
    //2. 다양한 선언
    vector<int> v; //크기가 0인 벡터
    vector<int> v2 = {2,3,4}; // 크기가 3인 지정값으로 초기화된 벡터
    vector<int> v3(10,5);   //크기가 10이고 초기값이 5로 선언된 벡터
    //3. 멤버 변수
    v.assign(5,2); // 2의 값으로 5개 원소 할당.
    v.at(1);    // 1번째 원소참조, 범위 벗어날 시 에러
    v.back();   // 마지막 원소 참조   
    v.push_back(5); // 변수 5를 맨 뒤에 추가.
    v.insert(v.begin()+2,0); //2번 position에 0 추가 후 이터레이터 반환.
    v.pop_back(); //마지막 원소 제거.
    v.erase(v.begin()+1); // iter(5)가 가리키는 원소 제거.
    v.clear();  // 모든 원소 제거, 그러나 메모리 남음.
    v.empty(); //vector가 비어있으면 true 리턴.
    return 0;
}