from typing import *
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        
        obst = set()
        dirs = [[0,1], [1,0], [0,-1], [-1,0]]
        cur_dir = 0 
        cur_pos = [0,0]
        distance = 0
        answer = 0

        for x, y in obstacles:
            obst.add((x,y))

        for i in range(len(commands)):
            if commands[i] == -1:
                cur_dir = (cur_dir + 1) % 4
            elif commands[i] == -2:
                cur_dir = (cur_dir - 1) % 4
            else:
                for i in range(commands[i]):
                    if (cur_pos[0] + dirs[cur_dir][0], cur_pos[1] + dirs[cur_dir][1]) in obst:
                        break
                    distance += 1
                    cur_pos = [cur_pos[0] + dirs[cur_dir][0], cur_pos[1] + dirs[cur_dir][1]]
                    answer = max(answer, pow(cur_pos[0], 2) + pow(cur_pos[1], 2))
        return answer
