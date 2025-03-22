#include <bits/stdc++.h>

using namespace std;   


#include <ext/pb_ds/assoc_container.hpp> 
#include <ext/pb_ds/tree_policy.hpp> 
using namespace __gnu_pbds; 
  
#define ordered_set tree<string, null_type,less_equal<int>, rb_tree_tag,tree_order_statistics_node_update> 
  


int main (){

    ordered_set myset;

    for (int i = 0; i < 10; i ++ ) {
        myset.insert(to_string(i));
    }   


    cout << *myset.find_by_order(3) << endl;
    // cout << myset.order_of_key(to_string(4)) << endl;


}