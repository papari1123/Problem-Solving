/*
-- 접근 방법--
얼마나 일반적인 규칙을 찾는지가 중요함.

[ME]
: 각 digit를 계수하여 최종 합을 구함.
: 0은 LS digit가 될 수 없으므로 예외 처리함.
[모범]
: A의 일의 자리 숫자가 0이고, B의 일의 자리 숫자가 9라면 
: 그 사이 0 ~ 9가 등장한 횟수는 모두 동일하게 (A/10 - B/10 + 1) 번이 됨.


-- 기타 문법 문제--
pow 함수는 double 형인데,

(int) = (int)/(double) -> 강제 int 형변환 
if((int)/(double)>0) -> double로 형변환 되서 문제 생김. 
pow(10,2) -> 99도 아니고 100도 아님.
-> 아래 아무것도 출력 안됨.
   if(100==pow(10,2))
        cout<<100;
    if(99==pow(10,2))
        cout<<99;     
*/

#include <iostream>
#include <vector>
#include <math.h>
using namespace std;
long long N;
long long num[10] = {0,}; 
long long long_pow(int base, int exp)
{
    long long result = 1;
    while (exp)
    {
        if (exp % 2)
           result *= base;
        exp /= 2;
        base *= base;
    }
    return result;
}

void add(int m)
{
    // m's digit의 개수를 구함.
     for(int i=0;i<=9;i++)
    {
        //cout<<"i:"<<i;
     
        if(i==0)
        { //0의 경우, 
            if(N/long_pow(10,m)<=9)
            { //LS digit인경우
                //skip
            }
            else
            {
            num[i] += max((N/long_pow(10,m+1)-1),(long long)0)*long_pow(10,m); //검사 자릿수보다 위
            num[i] += (((N/long_pow(10,m))%10)>i) ? long_pow(10,m) : 0;   
            num[i] += (((N/long_pow(10,m))%10)==i) ? (N%long_pow(10,m))+1 : 0;
            }
        }
        else
        { // 0 아닌 경우
             num[i] += (N/long_pow(10,m+1))*long_pow(10,m); //검사 자릿수보다 위
             num[i] += (((N/long_pow(10,m))%10)>i) ? long_pow(10,m) : 0;   
             num[i] += (((N/long_pow(10,m))%10)==i) ? (N%long_pow(10,m))+1 : 0;
        }
    }
}
int main(void)
{
    cin>>N;
    //0자리
    int m =0;

    while(N>=(long long)long_pow(10,m))
    {
        add(m);
        m++;     
    }
    for(int i=0;i<=9;i++)
    {
        cout<<num[i]<<" ";
    }
    return 0;
}