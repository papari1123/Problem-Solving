#include <iostream>
#include <vector>
#include <stack>

using namespace std;
int N, M;
vector<int> v;
bool visit[10] = { 0, };
int index = 0;
void fullsearch(int start, int num)
{
	for (int i = start;i<=N; i++)
	{
		if (visit[i] == 1)
			continue;
		v.push_back(i);
		visit[i] = 1;
		if (num == M)
		{
			for (auto ele : v)
			{
				cout << ele<<" ";
			}
			cout << "\n";
		}
		else
		{
			fullsearch(start, num + 1);
		}
		v.pop_back();
		visit[i] = 0;
	}
	
}
int main()
{
	cin>>N>>M;
	int cnt = 0;
	fullsearch(1,1);
	return 0;
}