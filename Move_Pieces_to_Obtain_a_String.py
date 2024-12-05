from typing import *

class Solution:
    def canChange(self, start: str, target: str) -> bool:
        top = []
        bottom = []
        for i in range(len(start)):
            if start[i] != '_':
                top.append([start[i], i])
            if target[i] != '_':
                bottom.append([target[i], i])
        if len(top) != len(bottom):
            return False
        for i in range(len(top)):
            if top[i][0] != bottom[i][0]:
                return False
            if top[i][0] == 'L':
                if top[i][1] < bottom[i][1]:
                    return False
            if top[i][0] == 'R':
                if top[i][1] > bottom[i][1]:
                    return False
        return True

