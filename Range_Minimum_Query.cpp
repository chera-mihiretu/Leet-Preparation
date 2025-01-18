#include <bits/stdc++.h> 
using namespace std;


#define ll long long
#define pb push_back
#define all(v) v.begin(), v.end()
#define rall(v) v.rbegin(), v.rend()
#define F first
#define S second
#define endl '\n'

const ll MOD = 1e9 + 7;
const ll INF = 1e18;


void fastIO() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
}


int main() {
    fastIO();

    int t = 1; 
    // cin >> t; 
    while (t--) {
        int n, q;
        cin >> n;
        vector<int> arr(n);

        for (int i = 0; i < n; ++i) cin >> arr[i];

        cin >> q;
        vector<pair<int, int>> query(q, pair<int, int>{});
        for (int i = 0; i < q; ++i  ) cin >> query[i].first >> query[i].second;


        // build the sparse tree

        int k = log2(n) + 1;
        vector<vector<int>> sparse(n, vector<int>(k, 0));

        for (int i = 0; i < n; ++i) sparse[i][0] = arr[i];

        
        for (int j = 1; j < k; ++j) {
            for (int i =0 ; i + (1 << j) - 1 < n; ++i) {
                
                sparse[i][j] = min(sparse[i][j-1], sparse[i + (1 << (j - 1))][j - 1]);
            }

        }
        

        // handle the query

        for (auto pos : query) {
            int L = pos.first;
            int R = pos.second;
            int dif = R - L + 1;
            int j = log2(dif);

            int answer = min(sparse[L][j],sparse[R-(1 << j) + 1][j] );

            cout << answer << endl;
        }

        
    }

    return 0;
}
