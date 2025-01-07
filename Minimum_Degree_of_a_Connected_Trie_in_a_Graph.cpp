#include <bits/stdc++.h>

using namespace std;




class Solution {
public:
    int minTrioDegree(int n, vector<vector<int>>& edges) {
        vector<bool> visited(n, false);
        queue<int> que;
        set<int> current;
        int answer = INT_MAX;
        vector<vector<int>> graph(n, vector<int>{});
        set<int> nodes;
        for (auto edge : edges) {
            auto [fr, to] = make_pair(edge[0]-1, edge[1]-1);
            
            
            graph[fr].push_back(to);
            graph[to].push_back(fr);
        }
        // for (auto edge : graph){
        //     cout << '[' << ' ';
        //     for (auto node : edge) cout << node << " ";
        //     cout << ']' << ' ';
        //     cout << endl;        
        // }
        for (int i = 0; i < n ; ++ i ){
            
            

            for (int child : graph[i]){
                if (visited[child]) continue;
                que.push(child);
                current.insert(child);
            }

            while (!que.empty()){
                int current_node = que.front();
                que.pop();

                for (int child : graph[current_node]){
                    
                    if (current.find(child) != current.end() && !visited[child]) {
                        int degreeCount = 0;
                        degreeCount += graph[current_node].size() - 2;
                        degreeCount += graph[child].size() - 2;
                        degreeCount += graph[i].size() - 2;
                        
                        
                        answer = min(answer, degreeCount);
                        
                    }
                }
            }

            visited[i] = true;



            
            current.clear();

        }

        if (answer == INT_MAX) return -1;
        return answer;
    }
};