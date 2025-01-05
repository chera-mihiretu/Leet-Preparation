// Lazy Heap 


#include <bits/stdc++.h>

using namespace std;



class TaskManager {
public:
    priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>> heap;
    map<int, int> last;
    map<int, int> user;
    TaskManager(vector<vector<int>>& tasks) {
        for (auto task : tasks) {
            int uid = task[0], tid = task[1], p = task[2];
            heap.push({p, tid, uid});
            last[tid] = p;

            user[tid] = uid;
        }
    }
    
    void add(int userId, int taskId, int priority) {
        int uid, tid, p;
        tie(uid, tid, p) = tuple<int, int, int>{userId, taskId, priority};
        heap.push({p, tid, uid});
        last[tid] = p;
        user[tid] = uid;
    }
    
    void edit(int taskId, int newPriority) {
        int uid = user[taskId];
        heap.push({newPriority, taskId, uid});
        last[taskId] = newPriority;
    }
    
    void rmv(int taskId) {
        last[taskId] = INT_MIN;
    }
    
    int execTop() {
        while (!heap.empty()){
            int p, tid, uid; 
            tie(p, tid, uid) = heap.top();
            heap.pop();
            if (last[tid] != p) continue;
            last[tid] = INT_MIN;
            return uid;
        }
        return -1;
    }
};

/**
 * Your TaskManager object will be instantiated and called as such:
 * TaskManager* obj = new TaskManager(tasks);
 * obj->add(userId,taskId,priority);
 * obj->edit(taskId,newPriority);
 * obj->rmv(taskId);
 * int param_4 = obj->execTop();
 */