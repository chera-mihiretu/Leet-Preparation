from typing import *


class Solution:
    def minChair(self, S, e) -> int:
        pref = [0] * (len(S) + 1)

        for i in range(len(S)):
            pref[]