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


#include <ext/pb_ds/assoc_container.hpp> 
#include <ext/pb_ds/tree_policy.hpp> 
using namespace __gnu_pbds; 
  
#define ordered_set tree<int, null_type,less_equal<int>, rb_tree_tag,tree_order_statistics_node_update> 
  

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
        int n;
        cin >> n;
        vector<int> arr(n);
        for (int i =0; i < n; ++i) cin >> arr[i];
        unordered_map<int, int> count_left;
        unordered_map<int, int> count_right;
        vector<int> left(n), right(n);
        ordered_set left_set;

        
        for(int i = 0; i < n; ++i){
            if (count_left.find(arr[i]) == count_left.end()) 
                count_left[arr[i]] = 0;
            
            count_left[arr[i]]++;

            left[i] = count_left[arr[i]];
        }

        for (int i = n -1; i >= 0; --i) {
            if(count_right.find(arr[i]) == count_right.end())
                count_right[arr[i]] = 0;
            count_right[arr[i]]++;

            right[i] = count_right[arr[i]];

        }

       

        ll answer = 0;
        for (int i = 0; i < n; ++ i ){
            
            int greater = left_set.size() - left_set.order_of_key(right[i] + 1);

            // cout <<  right[i] << ' ' << greater << endl;

            answer += greater;

            left_set.insert(left[i]);


        }   

        cout << answer << endl;
        
    }

    return 0;
}
