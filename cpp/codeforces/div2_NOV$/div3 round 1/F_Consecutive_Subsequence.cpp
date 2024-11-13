#include <bits/stdc++.h>
using namespace std;
void solve(){

    unordered_map<int, int> seqs;
    int length;
    cin >> length;
    vector<int> arr(length);

    for (int i=0; i < length; ++i) cin >> arr.at(i);


    for (int i=0; i < length; ++i ){
        int comp = arr.at(i) - 1;

        if (seqs.find(comp) != seqs.end()){
            int current = seqs[comp] + 1;
            if (seqs.find(arr.at(i)) != seqs.end()){
                seqs[arr.at(i)] = max(current, seqs[arr.at(i)]);
            }else{
                seqs[arr.at(i)] = current;
            }
        }else{
            seqs[arr.at(i)] = 1;
        }
    }
    int number = 0, count = 0;
    for (auto &nums : seqs){
        if (count < nums.second){
            count = nums.second; number = nums.first;
            // cout << nums.first << " " << nums.second << endl;
        }
    }

    int start = number - (count - 1);
    vector<int> answer;
    for (int i=0; i < arr.size(); ++i){
        if (arr.at(i) == start){
            answer.push_back(i + 1);
            start += 1;
        }
    }   
    cout << answer.size() << endl;

    for (auto num : answer){
        cout << num << " ";
    }
    cout << endl;

}

int main(){
    solve();
}