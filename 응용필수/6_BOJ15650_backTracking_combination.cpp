#include <iostream>
#include <vector>
#include <stack>
using namespace std;
int N, M;
vector<int> v;
void back(int start, int num)
{
	for (int i = start; i <= N - M + num; i++)
	{
		v.push_back(i);
		if (num == M)
		{
			for (auto ele : v)
			{
				cout << ele << " ";
			}
			cout << "\n";
		}
		else
		{
			back(i + 1, num + 1);
		}
		v.pop_back();
	}

}
int main()
{

	cin >> N >> M;
	int cnt = 0;
	back(1, 1);
	return 0;
}