class SegmentedTree:
    def __init__(self,arr):
        self.arr = arr
        self.n = len(arr)
        self.tree = [0 for i in range(4*self.n)]
        self.build(0, 0, self.n - 1)
    def build(self, node, arr_left, arr_right):
        if arr_left == arr_right:
            self.tree[node] = self.arr[arr_left]
            return 
        mid = arr_left + (arr_right - arr_left) // 2

        left_child, right_child = self.getChild(node)

        self.build(left_child, arr_left, mid)
        self.build(right_child, mid + 1, arr_right)

        self.tree[node] = self.tree[left_child] + self.tree[right_child]
    
    def getChild(self, node):
        left = 2 * node + 1
        right = 2 * node + 2
        return [left, right]
    
    def update(self, node, index, arr_left, arr_right, to):
        if arr_left == arr_right:
            self.arr[arr_left] = to
            self.tree[node] = self.arr[arr_left]
            return
        
        mid = arr_left + (arr_right - arr_left) // 2
        left_child, right_child = self.getChild(node)
        if index <= mid:
            self.update(left_child, index, arr_left, mid, to)
        else:
            self.update(right_child, index, mid + 1, arr_right, to)

        self.tree[node] = self.tree[left_child] + self.tree[right_child]

    def query(self, node, arr_left, arr_right, q_left, q_right):
        if q_left > q_right:
            return 0
        if q_left == arr_left and q_right == arr_right:
            return self.tree[node]
        mid = arr_left + (arr_right - arr_left) // 2
        left_child , right_child = self.getChild(node)
        left_result = self.query(self, left_child, arr_left, mid, q_left, min(mid, q_right))
        right_result = self.query(self, right_child, mid + 1, arr_right, max(mid + 1, q_left), q_right)
        return left_result + right_result
