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

    vector<int> color;
    vector<vector<int>> graph;
    vector<pair<int, int>> answer;
    vector<bool> visited;
    int t = 1; 
    // cin >> t; 
    while (t--) {

        int n, m , D;
        cin >> n >> m >> D;

        color.resize(n, -1);
        graph.resize(n, vector<int>{});
        visited.resize(n, false);



        
        while (m--) {
            int from, to;

            cin >> from >> to;

            from  -- ;
            to --;

            graph[from].push_back(to);
            graph[to].push_back(from);
        }

        int count = 0;
        queue<int> que;

        for (int i = 1; i < n; ++ i ){
            if (color[i] != -1) continue;

            que.push(i);
            
            color[i] = count;
            while (!que.empty()){
                int node = que.front();
                que.pop();
               
                
                for (int child : graph[node]){
                    if (child == 0) continue;
                    
                    if (color[child] == -1) {
                        que.push(child);
                        color[child] = count;
                    }

                }
            }
            count ++;
            
        }

        
        if (count > D || D > graph[0].size()){
            cout << "NO" << endl;
            break;
        }

        sort(graph[0].begin(), graph[0].end(), [&](const int& a, const int& b){
            return color[a] < color[b];
        });

        visited[0] = true;
        for (int i = 0; i < int(graph[0].size()); ++ i) {
            if (i == 0 || color[graph[0][i]] != color[graph[0][i-1]]){
                answer.push_back({0, graph[0][i]});
                que.push(graph[0][i]);
                visited[graph[0][i]] = true;
                D --;
            }
        }

        for (int i = 1; i < int(graph[0].size()); ++ i) {
            if (D == 0) break;
            if (color[graph[0][i]] == color[graph[0][i-1]]){
                answer.push_back({0, graph[0][i]});
                que.push(graph[0][i]);
                visited[graph[0][i]] = true;
                D --;
            }
        }

        cout << "YES" << endl;

        while (!que.empty()) {
            int node = que.front();
            que.pop();

            for (int c : graph[node]) {
                if (!visited[c]){
                    answer.push_back({node, c});
                    visited[c] = true;
                    que.push(c);
                }
            }
        }


        for (auto [a,  b] : answer) { 
            cout << a + 1 << ' ' << b + 1 << endl;
        }

        


        
    }

    return 0;
}
