#include <bits/stdc++.h>

using namespace std;


class SegmentedTree{
private:
    int* latest_index;
    int** from_to;
public:
    SegmentedTree(int n) {
        int tree_size = n * 4;
        latest_index = new int[tree_size];
        from_to = new int*[tree_size];
        for (int i = 0; i< tree_size; ++i) from_to[i] = new int[2];
    }

    SegmentedTree(){
        
    }
};


int  main(){
    int n, m;
    cin >> n >> m;

    vector<int> a(n);
    vector<int> b(n);

    for (int i = 0; i < n; ++ i) cin >> a[i];
    for (int i = 0; i < n; ++ i) cin >> b[i];

    while (m -- ) {
        int command; 
        cin >> command;

        if (command == 1) {
            int x, y, k;
            cin >> x >> y >> k;
            x--;y--;
            vector<int> temp;
            
        } else {
           int x;

           
        }
    }

}