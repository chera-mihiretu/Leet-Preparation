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

class UnionFind{

private:
    vector<int> parent;
public:
    UnionFind(int);
    int find(int);
    void unionThem(int, int);
};

UnionFind::UnionFind(int size){
    parent.resize(size, 0);

    iota(parent.begin(), parent.end(), 0);
}

int UnionFind::find(int a){
    if (parent[a] != a) {
        parent[a] = find(parent[a]);
    }
    return parent[a];
}

void UnionFind::unionThem(int a, int b) {
    
    
    parent[a] = b;
        
    
}


int main() {
    fastIO();

    int t = 1; 
    // cin >> t; 
    while (t--) {
        int n , m;
        cin >> n >> m;
        queue<int> que;


        UnionFind *uf = new UnionFind(n);
        vector<pair<int, int>> answer;
        vector<vector<int>> graph(n + 1 , vector<int>{});
        

        for (int i = 0; i < m; ++i ){

            int node_1, node_2;
            cin >> node_1 >> node_2;

            graph[node_1].push_back(node_2);
            graph[node_2].push_back(node_1);
        }

        int index = 0;
        for (int i = 0; i <= n; ++i) {
            if (graph[index].size() < graph[i].size()) {
                index = i;
            }
        }
        vector<int> arr (n + 1, false);

        arr[index] = true;
        // cout << index << endl;
        que.push(index);
        // for (auto g : graph) {for (auto c : g) cout << c << ' ' ; cout << endl;}
        while (!que.empty()){
            int n = que.front();
            que.pop();
            

            for (int& c : graph[n]) {
                if (!arr[c]) {
                    arr[c] = true;
                    que.push(c);
                    answer.push_back({n, c});
                }
            }
        }

        for (auto& [a, b] : answer) {
            cout << a << ' ' << b << endl;
        }


        
        
    }

    return 0;
}
