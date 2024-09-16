from typing import *
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timeInMinute = []
        for i in range(len(timePoints)):
            current = timePoints[i]
            hour, minute = current.split(':')
            minute_only= int(hour) * 60 + int(minute)
            timeInMinute.append(minute_only)
        timeInMinute.sort()
        answer = float('inf')
        for i in range(len(timeInMinute)):
            normal_diff =  abs(timeInMinute[i] - timeInMinute[i-1])
            circular_diff= abs((timeInMinute[i] + 24 * 60 )- timeInMinute[i-1])
            # print(timeInMinute)
            # print(normal_diff,  circular_diff, 24 * 60)
            answer = min(answer,normal_diff,circular_diff)
        return answer



## This problem can be solved using constant space and O(n) time complexity 
# this is by arrange the time as boolean array of length 24 * 60 wich is the minute  we have in a day
# after that we can use pointer to identify the defferenvce between the present times.
# 
#  




        
            


