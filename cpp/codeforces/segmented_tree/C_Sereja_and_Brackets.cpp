#include <bits/stdc++.h> 
using namespace std;


class SegmentedTree{
private:
    vector<tuple<int,int, int>> tree;
    string brackets;

    pair<int,int> getChild(int node){
        return {node * 2 + 1, node * 2 + 2};
    }
public:
    SegmentedTree(string brackets){
        this->brackets = brackets;
        tree.resize(brackets.size() * 4);
        this->build(0,0, brackets.size() - 1);
        // for (auto [a, b, c] : tree) cout << a << ' ' << b << ' ' << c << endl;
        
    }


    void build(int node, int left, int right){
        if (left == right) {
            if (this->brackets[left] == '(') {
                tree[node] = {1, 0, 0};
                return ;
            } else {
                tree[node] = {0, 1, 0};
                return ;
            }
        }

        int mid = left + (right - left) / 2;
        auto [left_child, right_child] = getChild(node);

        build(left_child, left, mid);
        build(right_child, mid + 1, right);


        int l_left, l_right, l_total, r_left, r_right, r_total;

        tie(l_left, l_right, l_total) = tree[left_child];
        tie(r_left, r_right, r_total) = tree[right_child];

        int new_left = max(0, l_left - r_right) + r_left;
        int new_right = max(0, r_right - l_left) + l_right;
        int new_total = l_total + r_total + 2 * min(l_left, r_right);

        this->tree[node] = {new_left, new_right, new_total};

        
    }


    tuple<int, int, int> query(int node, int left, int right, int l, int r){

        if (l > r){
            return {0,0,0};
        }

        if (l == left and r == right) {
            return tree[node];
        } 

        int mid = left + (right - left) / 2;
        auto [left_child, right_child] = getChild(node);

        auto [l_left, l_right, l_total] = query(left_child, left, mid, l, min(r, mid));
        auto [r_left, r_right, r_total] = query(right_child, mid + 1, right, max(l, mid + 1), r);
        int new_left = max(0, l_left - r_right) + r_left;
        int new_right = max(0, r_right - l_left) + l_right;
        int new_total = l_total + r_total + 2 * min(l_left, r_right);

        return {new_left, new_right, new_total};

    }







};

void fastIO(){
    ios::sync_with_stdio(false);

    cin.tie(nullptr);
    cout.tie(nullptr);
}

int main (){
    int m;
    string brackets;
    cin >> brackets >> m;
    SegmentedTree* t = new SegmentedTree(brackets);
    while (m -- ){
        int l, r;

        cin >> l >> r;
        l --; r --;

        auto [left, right, total] = t->query(0, 0, brackets.size() - 1, l, r);
        cout << total  << endl;


    }
}