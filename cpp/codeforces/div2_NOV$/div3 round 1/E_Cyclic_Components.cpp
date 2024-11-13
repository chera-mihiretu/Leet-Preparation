#include <bits/stdc++.h>

using namespace std;

bool nocircle = true;
int start = 0;
vector<vector<int>> graph;
unordered_set<int> visited;
void check(int node, int prev, bool &nocircle){

    if (graph[node].size() != 2){
        nocircle = false;
    }


    for (auto num : graph.at(node)){
        if (num != prev && visited.find(num) == visited.end()){
            visited.insert(num);
            check(num, node, nocircle);
        }
    }


}

void solve(){
    int n, m; 
    cin >> n >> m;

    graph.assign(n, {});

    for (int i = 0; i < m; ++i){
        int from, to;
        cin >> from >> to;
        from --; to --;

        graph.at(from).push_back(to);
        graph.at(to).push_back(from);
    }

    int count = 0;

    for (int i = 0; i < n; ++i){
        if (visited.find(i) == visited.end()){
            nocircle = true;
            visited.insert(i);
            check(i, -1, nocircle);
            if(nocircle) count += 1;
        }

    }

    std::cout << count << std::endl;


}
int main (){
    solve();
}