#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    void solve(int idx, int &N, vector<bool> &vis, int &n, bool &found, vector<int> &ans) {
        if(idx == N) {
            found = true;
            return;
        }
        if(ans[idx] != 0) {
            solve(idx + 1, N, vis, n, found, ans);
            return;
        }
        for(int num = n; num >= 1; num--) {
            if(!vis[num]) {
                vis[num] = true;
                if(num == 1) {
                    ans[idx] = num;
                    solve(idx + 1, N, vis, n, found, ans);
                    if(found) {
                        return;
                    }
                    ans[idx] = 0;
                }
                else if((idx + num) < N && ans[idx + num] == 0) {
                    ans[idx] = num;
                    ans[idx + num] = num;
                    solve(idx + 1, N, vis, n, found, ans);
                    if(found) {
                        return;
                    }
                    ans[idx] = 0;
                    ans[idx + num] = 0;
                }
                vis[num] = false;
            }
        }
    }

    vector<int> constructDistancedSequence(int n) {
        int N = (2 * n) - 1;
        vector<bool> vis(n + 1, false);
        vector<int> ans(N, 0);
        bool found = false;
        solve(0, N, vis, n, found, ans);
        return ans;
    }
};