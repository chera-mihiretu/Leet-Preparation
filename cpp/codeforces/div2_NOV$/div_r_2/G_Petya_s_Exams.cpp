#include <bits/stdc++.h>
#define all(x) (x).begin(), (x).end()
using namespace std;
void solve(){
    int n, m;

    vector<vector<int>> arr;
    arr.assign(n, {});


    for(int i = 0; i < m; i++){
        int a, b, c;
        cin >> a >> b>> c;

        arr[i].push_back(a);
        arr[i].push_back(b);
        arr[i].push_back(c);

    }   

    priority_queue<pair<int, int>, vector<pair<int, int>>,greater<int>> minHeap; 

    sort(all(arr));
    int index;
    for (int i = 1; i <= n; ++i){
        if (i == arr.at(index).at(0)){
            minHeap.push(pair<int, int>{arr.at(index).at(1), arr.at(index).at(2)});
        }

        pair<int, int> top = minHeap.top();
        minHeap.pop();
        
    }
    

}


int main (){
    solve();
}