#include <bits/stdc++.h>
using namespace std;
class Solution {
private:
    vector<vector<int>> grid;
    int m, n;
public:

    int countUnguarded(int m, int n, vector<vector<int>>& guards, vector<vector<int>>& walls) {
        grid.assign(m, vector<int>(n, 0));
        this->m = m;
        this->n  = n;
        for (vector<int> wall : walls){
            // cout << wall[0] << wall[1] << endl;
            grid[wall[0]][wall[1]] = -1;
        }
        for (auto guard : guards){
            grid[guard[0]][guard[1]] = 2;
        }

        for (int i = 0; i < m; ++i){
            for (int j = 0; j < n; ++j){
                if(grid[i][j] == 2){
                    // cout << i << ' ' << j << endl;
                    goToAll(i, j);
                }
            }
        }
        int answer = 0;

        for (int i = 0; i < m; ++i){
            for (int j = 0; j < n; ++j){
                if(grid[i][j] == 0){
                    answer += 1;
                }
            }
        }

           
        return answer;
    }

    void goToAll(int x, int y){
        move(x, y - 1, 'L');
        move(x, y + 1, 'R');
        move(x + 1, y, 'D');
        move(x - 1, y, 'U');
    }

    void move(int x, int y, char pos){
        if (x >= m || x < 0 || y < 0 || y >= n) return;
        if (grid[x][y] == -1 || grid[x][y] == 2) return;
        grid[x][y] = 1;
        if (pos == 'L'){
            move(x, y - 1, 'L');
        }else if (pos == 'R'){
            move(x, y + 1, 'R');
        }else if (pos == 'U') {
            move(x - 1, y, 'U');
        }else if (pos == 'D'){
            move(x + 1, y, 'D');
        }


    }
    
};