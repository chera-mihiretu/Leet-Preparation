#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) {
        int s = *max_element(nums.begin(), nums.end()) + 1;
        s ++ ;
        vector<pair<int, int>>  memo(s, {-1, -1});
        
        for ( int i = 0; i < nums.size(); ++ i ){
            memo[nums[i]] = {1, 1};
            for ( int j = 0; j < s; ++ j ){
                if (memo[j].first == -1) continue;
                if (nums[i] - j > 0){
                    memo[nums[i]].first = max(memo[nums[i]].first, memo[j].second + 1);
                }else if (nums[i] - j < 0) {
                    memo[nums[i]].second = max(memo[nums[i]].second, memo[j].first + 1);
                }
            }
        }
        int answer = 1;
        for (auto [s, e] : memo){
            answer = max({s,e,answer});
        }

        return answer;

    }
};

