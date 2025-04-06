#include <bits/stdc++.h>

using namespace std;
#define pb push_back
class Solution {
public:
    vector<int> largestDivisibleSubset(vector<int>& nums) {
        vector<int> prev(nums.size(), -1);
        vector<int> dp(nums.size(), 0);
        sort(nums.begin(), nums.end());
        int maxI = 0;
        for (int i = 0; i < nums.size(); ++i) {
            for (int j = 0; j < i; ++j) {
                if (nums[i] % nums[j] == 0 && dp[i] <= dp[j]) {
                    dp[i] = dp[j] + 1;
                    prev[i] = j;
                }

            }
            if (dp[maxI] < dp[i]) maxI = i;
        }

        int i = maxI;
        vector<int> answer;

        while ( i >= 0){
            answer.pb(nums[i]);
            i = prev[i];
        }

        return answer;
    }
};