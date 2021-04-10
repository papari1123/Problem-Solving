/* 
문제 : (implementation)
https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
풀이방법 : 

시간복잡도 :
O(N)

코멘트 :
시간복잡도를 최대한 줄인거 같은데, 더 간단한 풀이가 있을지는 모르겠음.
다른 풀이의 경우는, 스택을 이용하거나 바이너리 서치를 사용할수도 있음.
*/
#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

/*
 * Complete the 'climbingLeaderboard' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY ranked
 *  2. INTEGER_ARRAY player
 */




vector<int> climbingLeaderboard(vector<int> ranked, vector<int> player) {
    vector<int> ref_ranked(ranked.size());
    vector<int> result(player.size());
    //create ref_ranked
    ref_ranked[0] = 1;
     for(int i = 1;i<ranked.size(); i++)
    {
         static int rank = 1;
         if(ranked[i-1]>ranked[i])
         ref_ranked[i] = ++rank;
         else
         ref_ranked[i] = rank;
    }
 
    // compare
     for(int i = 0;i<player.size(); i++)
    { 
      static int last_ref_index = ranked.size()-1;   
      while(player[i]>=ranked[last_ref_index] && last_ref_index >= 0)
          last_ref_index--;
      result[i] = last_ref_index>= 0? ref_ranked[last_ref_index]+1 : 1;
    }
    return result;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string ranked_count_temp;
    getline(cin, ranked_count_temp);

    int ranked_count = stoi(ltrim(rtrim(ranked_count_temp)));

    string ranked_temp_temp;
    getline(cin, ranked_temp_temp);

    vector<string> ranked_temp = split(rtrim(ranked_temp_temp));

    vector<int> ranked(ranked_count);

    for (int i = 0; i < ranked_count; i++) {
        int ranked_item = stoi(ranked_temp[i]);

        ranked[i] = ranked_item;
    }

    string player_count_temp;
    getline(cin, player_count_temp);

    int player_count = stoi(ltrim(rtrim(player_count_temp)));

    string player_temp_temp;
    getline(cin, player_temp_temp);

    vector<string> player_temp = split(rtrim(player_temp_temp));

    vector<int> player(player_count);

    for (int i = 0; i < player_count; i++) {
        int player_item = stoi(player_temp[i]);

        player[i] = player_item;
    }

    vector<int> result = climbingLeaderboard(ranked, player);

    for (int i = 0; i < result.size(); i++) {
        fout << result[i];

        if (i != result.size() - 1) {
            fout << "\n";
        }
    }

    fout << "\n";

    fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}

vector<string> split(const string &str) {
    vector<string> tokens;

    string::size_type start = 0;
    string::size_type end = 0;

    while ((end = str.find(" ", start)) != string::npos) {
        tokens.push_back(str.substr(start, end - start));

        start = end + 1;
    }

    tokens.push_back(str.substr(start));

    return tokens;
}
