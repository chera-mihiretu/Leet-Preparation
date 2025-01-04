#include <bits/stdc++.h>

using namespace std;


class Solution {
public:
    int countPalindromicSubsequence(string s) {
        unordered_set<int> unique;
        int start, end, answer = 0;
        for (char c = 'a'; c <= 'z'; ++c){
            start= 0;
            end = s.length() - 1;
            while (start < end && (s[start] != c || s[end] != c)) {
                // cout << "- > " << c << " " << start << " " << end << endl;
                if (s[start] != c) start ++;
                if (s[end] != c) end --;
            }
            cout << c <<  " " << start << " " << end << endl;
            for (int i = start + 1; i < end; i ++ ){
                unique.insert(s[i]);
            }
            answer += unique.size();
            unique.clear();
        }
        return answer;
    }
};