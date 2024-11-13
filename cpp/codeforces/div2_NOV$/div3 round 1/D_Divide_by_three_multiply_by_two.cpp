#include <bits/stdc++.h>


using namespace std;
typedef long long mlong;
int main(){
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    int length;
    cin >> length;
    vector<pair<int, mlong>> nums;
    nums.assign(length, {});

    for (int i = 0; i < length; ++i){
        cin >> nums[i].second;

        int count = 0;
        mlong temp = nums[i].second;

        while (temp % 3 == 0) {
            count ++; 
            temp /= 3;
        }
        nums[i].first = -count;
        


    }   

    sort(nums.begin(), nums.end());


    for (auto num : nums) {
        cout << num.second << " ";
    }
    cout << endl;
    

}

// #include <bits/stdc++.h>
// using namespace std;
// typedef long long LL;
// int count3(LL x){
//   int ret=0;
//   while(x % 3 == 0){
//     ret++;
//     x /= 3;
//   }
//   return ret;
// }
// int n;
// vector<pair<int,LL>> v;
// int main(){
//   cin>>n;
//   v.resize(n);
//   for(int i=0; i<n; i++){
//     cin>>v[i].second;
//     v[i].first=-count3(v[i].second);
//   }
//   sort(v.begin(), v.end());
//   for(int i=0; i<n; i++)
//     cout << v[i].second << " " << v[i].first << " ";
// }