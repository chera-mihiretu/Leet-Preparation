from typing import *

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer = []
        for i in range(len(prices)):
            next = i + 1
            while next < len(prices) and prices[next] > prices[i]:
                next += 1
            result = 0
            if next < len(prices):
                result = prices[next]
            answer.append(prices[i] - result)
        return answer