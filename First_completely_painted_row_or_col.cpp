#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int firstCompleteIndex(vector<int>& arr, vector<vector<int>>& mat) {
        int N = mat.size(), M = mat[0].size();
        vector<int> row(N, 0);
        vector<int> col(M, 0);

        vector<pair<int, int>> map(M * N,pair<int,int>{});

        for (int i = 0; i < N; ++i ){
            for (int j = 0 ; j < M; ++ j ){
                map[mat[i][j] - 1] = make_pair(i, j);
            }
        }
        for (int i = 0; i < N * M; ++ i ){
            auto [F, S] = map[arr[i] - 1];

            row[F] ++;
            col[S] ++;

            if (row[F] == M)  return i;

            if (col[S] == N) return i;
        }

        return -1;

    }
};