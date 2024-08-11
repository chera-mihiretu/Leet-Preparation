from typing import *
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        intervals = []
        word_count = 0
        chars = 0
        for i in range(len(words)):
            if chars + (word_count) + len(words[i]) > maxWidth:
                space = maxWidth - chars 
                intervals.append([i, space])
                word_count = 1
                chars = len(words[i])
            else:
                chars += len(words[i])
                word_count += 1
        if chars != 0:
            intervals.append([i + 1, maxWidth - chars])


        print(intervals)

        answer = []
        pre = 0
        for i in range(len(intervals)):
            last_index = intervals[i][0]
            space = 0
            remain = 0
            if ((intervals[i][0] - pre) - 1) == 0: 

                space = ' ' * intervals[i][1]
            else:
                space = ' ' * (intervals[i][1] // ((intervals[i][0] - pre) - 1))
                remain = intervals[i][1] % ((intervals[i][0] - pre) - 1)
            row = []
            if i != len(intervals) - 1:
                for j in range(pre, last_index):
                    row.append(words[j])
                    if j != last_index - 1 or ((intervals[i][0] - pre) - 1) == 0:
                        row.append(space)
                    if remain:
                        row.append(' ')
                        remain -= 1
            else:
                left = remain
                space = intervals[i][1]
                for j in range(pre, last_index):
                    row.append(words[j])
                    if j != last_index - 1:
                        row.append(' ')
                        space -= 1
                    
                row.append(' ' * space)


            answer.append(row)
            pre = last_index
        final_result = [''.join(i) for i in answer]
        return final_result
                

        

