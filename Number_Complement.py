from typing import *
from math import log2, floor

class Solution:
    def findComplement(self, num: int) -> int:
        times = floor(log2(num)) + 1
        bit = 1 << times
        bit = bit - 1
        return num ^ bit
