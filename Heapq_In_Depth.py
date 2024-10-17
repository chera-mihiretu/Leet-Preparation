from typing import *
from heapq import * 
from random import randint as rand



nums = [10, 15, 1, 18, 9, 3, 12, 5, 15, 6, 12, 12, 15, 15, 16, 14, 17, 7, 13, 16]



class MyHeap:
    def __init__(self, nums):
        self.nums = nums
        heapify(self.nums)

    def heapify(self):
        return heapify(self.nums[::])
    # returns the nth maximum no need to heapify
    def maxNth(self):
        return nlargest(5, self.nums[::])
    # returns the nth minimum number no need to heapify
    def minNth(self):
        return nsmallest(5, self.nums[::])
    

x = MyHeap(nums)

print(x.minNth())