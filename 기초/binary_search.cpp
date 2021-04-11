#include <iostream>
#include <vector>
using namespace std;
//size 크기의 data배열안에서 d를 찾기
//값이없으면 -1반환
//값이 있으면 data배열의 index 반환
int binarySearch(vector<int> data, int size, int d)
{ 
    int start = 0;
    int end = size-1;
    int mid;
    while(start <= end)
    {
        mid = (start+end)/2;
        if(data[mid]==d)
           return mid;
        else if(data[mid]<d)
           start = mid + 1;
        else
           end = mid - 1;
    }
    return -1; // no result.
}
 
int main() {
    vector<int> data = { 1,3,6,8,11,23,112,114 };
    int ans = binarySearch(data, data.size(), 6);
    printf("%d\n", ans);
}