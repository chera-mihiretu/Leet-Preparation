from typing import *

class Solution:
    def maximumTime(self, time: str) -> str:
        self.places = []
        for i in time:
            if i ==':':
                continue
            self.places.append(i)
        for i in range(len(self.places)):
            if self.places[i] == '?':
                if i == 0:
                    self.places[i] = self.forFirstIndex()
                elif i == 1:
                    self.places[i] = self.forSecondIndex()
                elif i == 2:
                    self.places[i] = self.forThirdIndex()
                else:
                    self.places[i] = self.forFourthIndex()
        return ''.join(self.places[:2]) + ':' + ''.join(self.places[2:])
    def forFirstIndex(self):

        if self.places[1] == '?' or self.places[1] < '4':
            return '2'
        return '1'
    def forSecondIndex(self):
        if self.places[0] == '2':
            return '3'
        return '9'
    def forThirdIndex(self):
        return '5'
    def forFourthIndex(self):
        return '9'