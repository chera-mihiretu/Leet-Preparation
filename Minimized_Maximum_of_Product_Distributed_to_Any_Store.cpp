#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minimizedMaximum(int n, vector<int>& quantities) {
        int end = 0;
        int start = 1;
        for (auto num: quantities) end = max(end, num);
        int answer = 0;
        while (start <= end){
            int mid = start + (end - start) / 2;
            int curr_n = 0;
            // std::cout << mid << std::endl;
            for (int num : quantities){
                curr_n += ceil((static_cast<float>(num) / mid));
                //std::cout << mid << " " << num << " " << ceil((static_cast<float>(num) / mid)) << std::endl;
            }

            // std::cout << "This is the "<<  curr_n << std::endl;

            if (curr_n <= n){
                end = mid - 1;
                answer = mid;
            }else{
                start = mid + 1;
            }

        }

        return answer;

    }
};