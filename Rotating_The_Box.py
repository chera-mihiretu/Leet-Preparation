from typing import *
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        answer = [['.' for i in range(len(box))] for i in range(len(box[0]))]

        for  i in range(len(box)):
            for j in range(len(box[0])):
                answer[j][i] = box[i][j]
        for row in answer:
            row.reverse()
        

        for i in range(len(answer[0])):
            top = len(answer) - 1
            below = len(answer) - 1
            while top >= 0:
                if answer[top][i] == '*':
                    below = top - 1
                elif answer[top][i] == '#':
                    answer[top][i], answer[below][i] = answer[below][i], answer[top][i]
                    below -= 1
                top -= 1
        return answer
