class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        nums_odd = []
        nums_even = []
        target_odd = []
        target_even = []
        for i in range(len(nums)):
            if nums[i] & 1:
                nums_odd.append(nums[i])
            else:
                nums_even.append(nums[i])
            if target[i] & 1:
                target_odd.append(target[i])
            else:
                target_even.append(target[i])
        nums_odd.sort()
        nums_even.sort()
        target_even.sort()
        target_odd.sort()

        answer = 0
        current = 0
        for i in range(len(nums_even)):
            result = nums_even[i] - target_even[i]
            if result > 0:
                current += result
        answer = current // 2
        current = 0
        for i in range(len(nums_odd)):
            result = nums_odd[i] - target_odd[i]
            if result > 0:
                current += result
        answer += current // 2
        return answer
                

        