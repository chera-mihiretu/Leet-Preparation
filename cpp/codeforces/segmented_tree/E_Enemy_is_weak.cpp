#include <bits/stdc++.h> 

#define ll long long 
#define pb push_back

#include <ext/pb_ds/assoc_container.hpp> 
#include <ext/pb_ds/tree_policy.hpp> 
using namespace __gnu_pbds; 
  
#define ordered_set tree<ll, null_type,less<ll>, rb_tree_tag,tree_order_statistics_node_update> 
  

using namespace std;

void fastIO(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
}

int main(){

    fastIO();

    int n; 
    cin >> n; 
    vector<int> arr(n);



    for (int i = 0; i < n; i++ ) cin >> arr[i];

    ordered_set lset;
    ordered_set rset;

    for (int i = 0; i < n; i ++) {
        rset.insert(arr[i]);
    }

    ll answer = 0;
    for (int i = 0; i < n; i ++ ) {
        rset.erase(arr[i]);

        ll right = rset.order_of_key(arr[i]);
        ll left = lset.size() - lset.order_of_key(arr[i]);

        lset.insert(arr[i]);
        answer += left * right;
    }


    cout << answer << endl; 




}