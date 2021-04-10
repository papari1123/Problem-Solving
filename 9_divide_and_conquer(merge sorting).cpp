/**
 *  1.분할 : 주어진 문제를 동일한 방식으로 해결할 수 있는 여러 부분 문제로 나눈다.
 *  2.정복 : 각 부분 문제에 대한 해답을 구한다.
 *  3.결합 : 각 부분 문제의 해답을 결합하여 전체 문제에 대한 해답을 구한다.
 * 
 *  대표문제 : 병합정렬, 이진탐색, 맵리듀스
 *  여기서는 병합정렬을 예제로 둠.
 **/
#include <iostream>
#include <vector>
#include <queue>
using namespace std;
vector<int> v = {1,5,4,2,7,8,3,231,2,123,443,212,9,11,412,23,34,123,12,432,12,65,32,75,96,46,134,864,3,56,8,6,7,44,0};
void merge(vector<int> &v, int left, int mid, int right)
{
    static queue<int> q;
    int i = left;
    int j = mid+1; 
    while(i<=mid&&j<=right)
    { //각 부분간의 비교 수행
        if(v[i]<v[j])
        {
            q.push(v[i]);
            i++;
        }
        else
        {
            q.push(v[j]);
            j++;
        }
    }     
    if(i<=mid)
    { //남은 원소 복사
        while(i<=mid)
        {
            q.push(v[i]);
            i++;
        }   
    }
    else
    {
        while(j<=right)
        {
            q.push(v[j]);
            j++;
        }       
    }
    for(int k=left;k<=right;k++)
    { // 복사한 배열 대입
        v[k]= q.front();
        q.pop();
    }
    
}
void merge_sort(vector<int> &v, int left, int right)
{
    if(left<right)
    {
        int m = (left+right)/2; // 1.분할
        merge_sort(v,left,m); // 2. 정복
        merge_sort(v,m+1,right); // 2.정복
        merge(v,left,m,right); //3. 결합
    }
}
int main(void)
{
    merge_sort(v,0,v.size()-1);
    for(auto ele : v)
    {
        cout<<ele<<" ";
    }
    cout<<endl;
    return 0;
}
