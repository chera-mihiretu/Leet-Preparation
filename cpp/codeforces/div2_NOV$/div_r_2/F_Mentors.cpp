#include <bits/stdc++.h>

using namespace std;
void solve(){
    int n, k;
    cin >> n >> k;   
    vector<int> arr(n);
    vector<int> smaller;
    smaller.assign(n, 0);
    for (int i = 0; i < n; ++i){
        cin >> arr[i];
    }

    for (int i = 0; i < k; ++i){
        int from, to;

        cin >> from >> to;

        if (arr[from - 1] > arr[to - 1]){
            smaller[from - 1]++;
        }else if (arr[from - 1] < arr[to - 1]){
            smaller[to - 1]++;
        }
    }
    vector<int> sorted = arr;
    sort(sorted.begin(), sorted.end());
    vector<int> answer(n);
    for (int i = 0; i < n; ++i){
        int index = lower_bound(sorted.begin(), sorted.end(), arr[i]) - sorted.begin();
        answer[i] = index - smaller[i];
    }

    for (auto i : answer){
        cout << i << " ";
    }

    cout << endl;


}

int main(){
    solve();
}