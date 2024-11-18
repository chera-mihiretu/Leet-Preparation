#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<int> decrypt(vector<int>& code, int k) {
        int start = 1, end = k;
        int n = code.size();
        if (k < 0){
            start = n + k;
            end = n -1;
        }
        vector<int> answer(n);
        int total = 0;
        for (int i = start; i <= end; ++i){
            total += code[(i%n)];
        }
        for (int i = 0; i < n; ++i){
            answer.at(i) = total;
            total -= code[(start%n)];
            start++;
            end++;
            total += code[(end%n)];

            cout << total << endl;
        }
        return answer;
    }
};