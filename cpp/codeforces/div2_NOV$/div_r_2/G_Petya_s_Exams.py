from sys import stdin,stdout
from heapq import *
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n, m = [int(i) for i in input().split()]
    array = []
    exam = set()
    for row in range(m):
        a, b, c = [int(i) for i in input().split()]
        array.append([a, b, c, row + 1])
        exam.add(b)

    array.sort()
    heap = []
    result = [0 for i in range(n)]
    index = 0
    # print(array)
    for i in range(1, n + 1):
        
        while index < m and array[index][0] == i:
            
            heappush(heap, [array[index][1], array[index][2], array[index][3]])
            index += 1
        
        if i in exam:
            continue
        # print('HEAP LENG',heap, i, n)
        if heap:
            # print('before', heap)
            end, preparation, ans_ind = heappop(heap)
            # print('after',end, preparation, index)
            if end <= i:
                return [-1]
            if preparation - 1 > 0:
                heappush(heap, [end, preparation - 1, ans_ind])
            result[i-1] = ans_ind
    if heap:
        return [-1]
    for i in exam:
        result[i-1] = m + 1
    return result
            






# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        print(*solution())