#include <bits/stdc++.h>

class Solution {
public:
    bool canSortArray(vector<int>& nums) {
        std::vector<int> bitCount;
        
        int prev = countIt(nums.at(0));
        int prevMin =  INT_MAX;
        int prevMax =  INT_MIN;
        int pos = 0;
        bitCount.push_back(-1);
        nums.push_back((1 << 10) - 1);
        for (int i =1; i < nums.size(); ++i) {

            int currentMin = INT_MAX, currentMax = INT_MIN; 
            
            if (countIt(nums.at(i)) != prev){
                for (int j = pos; j < i; ++j){
                    currentMin = std::min(currentMin, nums.at(j));
                    currentMax = std::max(currentMax, nums.at(j));
                }
                if (currentMin < prevMax){
                    return false;
                }
                prevMin = currentMin;
                prevMax = currentMax;
                pos = i;
                prev = countIt(nums.at(i));
            }



        }

        return true;
    }

    int countIt(int number){
        int count = 0;
        while (number){
            count += number & 1;
            number >>= 1;
        }

        return count;
    }
};