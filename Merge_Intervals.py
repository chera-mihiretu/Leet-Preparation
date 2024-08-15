class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        start = intervals[0][0]
        end = intervals[0][1]
        answer = []
        for i in range(1, len(intervals)):
            if end >= intervals[i][0]:
                end = max(end, intervals[i][1])
            else:
                answer.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]
        answer.append([start, end])
        return answer
