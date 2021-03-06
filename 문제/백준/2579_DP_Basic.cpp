
/*
DP 기본

** 0번째가 아닌 첫번째부터 조건이 달린 문제는
 index또한 1부터 시작하게 해야 안 헷갈림.
*/
#include <iostream>
#include <vector>
#include <stack>
#include <math.h>

#define UNKNOWN -1

using namespace std;
int N;
vector<int> score;
vector<pair<int, int>> sum;
int max(int a, int b)
{
	return (a > b) ? a : b;
}

int getSum(int n, int con)
{
	if (con == 0)
	{
		if (sum[n].first != UNKNOWN)
			return sum[n].first;
		sum[n].first = getSum(n - 2, 1) + score[n];
		return sum[n].first;
	}
	else // con == 1
	{
		if (sum[n].second != UNKNOWN)
			return sum[n].second;
		sum[n].second = max(getSum(n - 1, 0), getSum(n - 2, 1)) + score[n];
		return sum[n].second;
	}
}
int main()
{
	cin >> N;
	//index N 맞추기 위한 dummy
	score.push_back(UNKNOWN);
	sum.push_back({ UNKNOWN, UNKNOWN });
	for (int i = 1; i <= N; i++)
	{
		int temp;
		cin >> temp;
		score.push_back(temp);
		sum.push_back({ UNKNOWN, UNKNOWN });
	}
	sum[1].first = score[1];
	sum[1].second = score[1]; //dummy
	sum[2].first = score[2];
	sum[2].second = score[1] + score[2];
	cout << max(getSum(N, 0), getSum(N, 1));
	return 0;
}