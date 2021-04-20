#include <iosteam>
//https://blockdmask.tistory.com/76
/*
0. list는 list 헤더를 사용한다.
*/
#include <list>

using namespace std;

int main(void)
{
    //1. 선언의 기본은 : list< [Data Type] > [변수 이름];
    list<int> lti;
    list<string> lts;
    //2. list 생성
    list<int> ltTest(10); // 원소 10개의 list 생성
    list<int> ltTest2(10,2); // 2로 초기화된 원소 10개 list 생성
    list<int> ltc(ltTest); //ltTest를 복사함.

    int k = 1;
    int n = ltTest.size();
    int iter = ltTest.begin();
    //3. 멤버 함수    
    ltTest.assign(2,2); // 2로 초기화된 2개의 원소를 할당함.
    ltTest.front(); //맨 앞의 원소를 반환함.
    ltTest.back();  //맨 뒤의 원소를 반환함.
    ltTest.begin(); //맨 앞 원소의 iterator를 반환.
    ltTest.end();   //맨 뒤 원소의 iterator를 반환.

    ltTest.push_back(k); //뒤쪽에 k를 삽입. O(n).
    ltTest.push_front(k);//앞쪽에 k를 삽입.

    ltTest.pop_back(); // 맨 뒤 원소를 제거.
    ltTest.pop_front();// 맨 앞 원소를 제거.

    ltTest.insert(iter,k); // iter가 가리키는 위치에 k를 삽입.
    ltTest.erase(iter); // iter가 가리키는 위치 원소를 삭제하고 원소 다음을 가리키는 iterator 반환.
   
    ltTest.size(); // 원소 개수를 반환.
    ltTest.remove(k); //k와 동일 원소 모두 제거.
    
    ltTest.remove_if(predicate); // predicate 조건자에 따라 제거
    bool predicate(int num){
    return num>=10 && num<=20;

    ltTest.reverse(); //원소의 순차열을 뒤집음.
    ltTest.sort();    // 원소를 오름차순으로 정렬.
    ltTest.sort(std::greater<int>()); //int원소들에 대해 내림차순으로 정렬.
}
}

