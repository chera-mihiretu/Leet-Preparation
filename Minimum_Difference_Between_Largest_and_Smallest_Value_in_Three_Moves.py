from typing import *
from heapq import *
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
       
        # collecting the numbers by reversing their values into negative 
        nums1 = []
        for i in range(len(nums)):
            nums1.append(-nums[i])
        nums2 = nums[::]
        # heapify both numbers to apply heap operation 
        heapify(nums1)
        heapify(nums2)

        # this will hold the values that are popped for temporary comparision 
        min_holder = []
        max_holder = []
         # answer hodler
        answer = (-nums1[0]) - nums2[0]
        # take 3 from  minheap only
        for i in range(3):
            min_holder.append(heappop(nums1))
        answer = min(answer, (-nums1[0]) - nums2[0] )
        self.returnRemovedValues(nums1, min_holder)



        # take 2 from minheap and 1 from max_heap
        for i in range(2):
            min_holder.append(heappop(nums1))
            if i == 0:
                max_holder.append(heappop(nums2))
        answer = min(answer, (-nums1[0]) - nums2[0] )
        self.returnRemovedValues(nums2, max_holder)
        self.returnRemovedValues(nums1, min_holder)
        

        # take 1 from minheap and 2 from max_heap
        for i in range(2):
            max_holder.append(heappop(nums2))
            if i == 0:
                min_holder.append(heappop(nums1))
        answer = min(answer, (-nums1[0]) - nums2[0])
        self.returnRemovedValues(nums2, max_holder)
        self.returnRemovedValues(nums1, min_holder)
        # take 0 from min heap and 3 from max_heap

        for i in range(3):
            max_holder.append(heappop(nums2))
        answer = min(answer, (-nums1[0]) - nums2[0] )
        self.returnRemovedValues(nums2, max_holder)

        return answer

        # Time Complexity = O(n)
        # Space Complexity = O(n)
    def returnRemovedValues(self, fromArray, toBeReturned):
        while toBeReturned:
            heappush(fromArray, toBeReturned.pop())


# This is after know the heap nth largest element function 

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0

        # Time Complexity is O(n)
        # Space Complexity is O(1)

        # We are gonna iterate over only the four elemts from both minimum and smallest
        four_small = nsmallest(4, nums)
        four_large = nlargest(4, nums)
        answer = four_large[0] - four_small[0]
        for i in range(4):
            answer = min(answer, four_large[i] - four_small[3 - i])
        return answer