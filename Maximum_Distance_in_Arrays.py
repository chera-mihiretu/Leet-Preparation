class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_num = arrays[0][0]
        max_num = arrays[0][-1]
        answer = 0
        for i in range(1, len(arrays)):
            answer = max(answer, abs(arrays[i][0] - max_num))
            answer = max(answer, abs(arrays[i][-1] - min_num))

            max_num = max(max_num, arrays[i][-1])
            min_num = min(min_num, arrays[i][0])
        return answer
