#include <bits/stdc++.h>
#define F first 
#define S second
using namespace std;


class SegmentedTree{
private:
    int* latest_index;
    int** from_to;
    int n;
    pair<int,int> getChild(int node){
        return pair<int,int>{
            node * 2 + 1, 
            node * 2 + 2
        };
    } 
    void _update(int node, int left, int right, int a_L, int a_R, int b_L, int b_R, int index) {
        if (b_L > b_R) return;
        if (left == b_L && right == b_R) {
            latest_index[node] = index;
            from_to[node][0] = a_L;
            from_to[node][1] = a_R;

            return;
        }

        int mid = left + (right - left) / 2;
        auto [left_child, right_child] = this->getChild(node);
        
        int left_diff = max(b_L, mid + 1) - b_L;
        int right_diff = b_R - min(mid, b_R);


        _update(left_child, left, mid, a_L, a_R - right_diff, b_L, min(mid, b_R), index);
        _update(right_child, mid + 1, right, a_L + left_diff, a_R, max(b_L, mid + 1), b_R, index);
        

    }
    pair<int, int> _getLatestIndex(int node, int left, int right, int index){
        if (left==right) {
            if ( latest_index[node] == -1){
                return {latest_index[node], index};
            }else{
                return {latest_index[node], from_to[node][0]};
            }
        }

        int mid = left + (right - left) / 2;

        auto [left_child, right_child] = this->getChild(node);


        if (index <= mid) {
            auto result = _getLatestIndex(left_child, left, mid, index);
            
            if (result.F >= latest_index[node]) {
                return result;
            }else{
                int cur_pos = index - left;
                int cur = latest_index[node];
                
                return pair<int, int>{latest_index[node], from_to[node][0] + cur_pos};
            }
        }else{
            auto result = _getLatestIndex(right_child, mid + 1, right, index);
            int cur = latest_index[node];
            if (result.F >= latest_index[node]) {
                return result;
            }else{
                int cur_pos = index - left;
                
                return pair<int, int>{latest_index[node], from_to[node][0] + cur_pos};
            }
        }


    }
public:
    SegmentedTree(int n) {
        this->n = n;
        int tree_size = n * 4;
        latest_index = new int[tree_size];
        from_to = new int*[tree_size];
        for (int i = 0; i< tree_size; ++i) from_to[i] = new int[2];


        for (int i  =0; i < tree_size; ++i){
            latest_index[i] = -1;
            from_to[i][0] = -1;
            from_to[i][1] = -1;
        }
    }

    void update(int i, int x, int y, int k) {
        this->_update(0, 0, n -1, x, x + k - 1, y, y + k -1, i);
    }


    pair<int, int> getLatestIndex(int pos){
        return this->_getLatestIndex(0, 0, this->n - 1, pos);
    }
    

    
    

    
};


int  main(){
    int n, m;
    scanf("%d %d", &n, &m);


    int a[n];
    int b[n];

    for (int i = 0; i < n; ++i) scanf("%d", a + i);
    for (int i = 0; i < n; ++i) scanf("%d", b + i);


    SegmentedTree* st = new SegmentedTree(n);


    for (int i = 0; i < m; ++ i) {
        int command;
        scanf("%d", &command);

        if (command == 1) {
            int x, y, k;
            scanf("%d %d %d", &x, &y, &k);

            st->update(i, x - 1, y - 1, k);

        } else{
            int pos;
            scanf("%d", &pos);

            pair<int, int> ind_pos = st->getLatestIndex(pos - 1);
            // printf("%d %d\n", ind_pos.F, ind_pos.S);
            if (ind_pos.F == -1) {
                printf("%d\n", b[ind_pos.S]);
            }else{
                printf("%d\n", a[ind_pos.S]);

            }
        }
    }


}