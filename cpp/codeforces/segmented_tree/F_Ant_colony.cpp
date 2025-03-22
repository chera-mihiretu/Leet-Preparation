#include <bits/stdc++.h>

using namespace std;
void fastIO(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
}





int main (){

    int n;
    cin >> n;
    vector<int> arr(n);
    int COL = log2(n) + 1;
    vector<vector<int>> min_sparce(n, vector<int>(COL));
    vector<vector<int>> gcd_sparce(n, vector<int>(COL));
    unordered_map<int, vector<int>> num_pos;
    
    for (int i = 0; i < n; ++i ) cin >> arr[i];
    int m;
    cin >> m;


    for (int i =0; i < n; ++i) {
        if (num_pos.find(arr[i]) == num_pos.end()) {
            num_pos[arr[i]] = vector<int>();
        }
        num_pos[arr[i]].push_back(i);
        min_sparce[i][0] = arr[i];
        gcd_sparce[i][0] = arr[i]; 
    }

    for (int j = 1; j < COL; ++ j) {
        for (int i = 0; i + (1 << j) - 1 < n; ++i ){
            min_sparce[i][j] = min(min_sparce[i][j-1], min_sparce[i + (1 << (j - 1))][j - 1]);
            gcd_sparce[i][j] = gcd(gcd_sparce[i][j-1], gcd_sparce[i + (1 << (j - 1))][j - 1]);
        }
    }

   


    while (m -- ){
        int L, R;
        cin >> L >> R;
        L--;R--;
        int distance = R - L + 1;

        int step = log2(distance);


        int range_gcd = gcd(gcd_sparce[L][step], gcd_sparce[R - (1 << step) + 1][step]);
        int range_min = min(min_sparce[L][step], min_sparce[R - (1 << step) + 1][step]);

        if (range_gcd == range_min) {
            int  left = lower_bound(num_pos[range_min].begin(), num_pos[range_min].end(), L) - num_pos[range_min].begin();
            int right = upper_bound(num_pos[range_min].begin(), num_pos[range_min].end(), R) - num_pos[range_min].begin();
            
            int answer = right - left;
            // cout << range_gcd << ' ' << range_min << ' ' << left << ' ' << right <<  endl;
            cout << (R - L + 1) - answer << endl;
            
        }else{
            cout << R - L + 1 << endl;
        }


    }


}