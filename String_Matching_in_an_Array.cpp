#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<string> stringMatching(vector<string>& words) {
        sort(words.begin(), words.end(), [](const string a, const string b){
            return a.length() < b.length();
        });
        vector<string> answer;
        for (int i = 0; i < words.size(); ++ i ){
            for (int j = i + 1; j < words.size(); ++ j ) {
                if (words[j].find(words[i]) != string::npos) {
                    answer.push_back(words[i]);
                    break;
                }
            }
        }
        return answer;
    }
};