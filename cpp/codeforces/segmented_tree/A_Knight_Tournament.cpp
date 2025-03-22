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
        int n, m;

        cin >> n >> m;

        vector<int> answer(n, 0);
        vector<tuple<int, int, int>> queries;

        for (int i = 0; i < m; i ++) {
            int l, r, x;
            cin >> l >> r >> x;
            queries.pb({l, r, x});
        }

        set<int> content;

        for (int i = 1; i <= n; i ++){
            content.insert(i);
        }

        for (int i = 0; i < m; i++) {
            int l, r, x;
            tie(l,r,x) = queries[i];
            r ++;
            vector<int> removed;

            for (set<int>::iterator it = content.lower_bound(l); it != content.end() && *it < r; it ++){
                if (*it != x) {
                    answer[*it - 1] = x;
                    removed.pb(*it);
                }
            }

            for (auto& c : removed) {
                content.erase(c);
            }
        }


        for (auto &a : answer) {
            cout << a << " ";
        }
        cout << endl;
        
    }

    return 0;
}
