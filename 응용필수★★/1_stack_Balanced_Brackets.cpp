#include <bits/stdc++.h>

// stack 이용한 문제. medium이라고 하기엔 쉬움.
using namespace std;

// Complete the isBalanced function below.
string isBalanced(string s) {
    stack<char> brackets;
    int size  = s.size();
    for(int i=0;i<size;i++)
    {
     if(s[i]=='(' || s[i]=='{' || s[i]=='[')
         brackets.push(s[i]);
     else if(brackets.empty())
         return "NO";
     else if((s[i]==')' && brackets.top()=='(')
         ||(s[i]==']' && brackets.top()=='[')
         ||(s[i]=='}' && brackets.top()=='{'))
             brackets.pop();
     else
         return "NO";
     }
    if(brackets.empty())
         return "YES";
     else 
         return "NO";
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int t;
    cin >> t;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    for (int t_itr = 0; t_itr < t; t_itr++) {
        string s;
        getline(cin, s);

        string result = isBalanced(s);

        fout << result << "\n";
    }

    fout.close();

    return 0;
}
