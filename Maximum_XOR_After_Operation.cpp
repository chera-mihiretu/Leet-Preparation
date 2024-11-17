
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maximumXOR(vector<int>& nums) {
        int xored = 0;
        for(int i =0; i < nums.size(); ++i){
            int temp = nums[i];
            int count = 0;
            while (temp){
                if (temp & 1){
                    xored |= (1 << count);
                    
                }
                temp >>= 1;
                count += 1;
            }
        }
        return xored;
    }
};