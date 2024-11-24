from typing import *

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total = neg_count = 0
        minimum = float('inf')
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                total += abs(matrix[i][j])
                neg_count += 1 if matrix[i][j] < 0 else 0
                minimum = min(minimum, abs(matrix[i][j]))
        if neg_count & 1:
            # print('here', total)
            total -= 2 * minimum
        return total