from typing import * 
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        M = 9
        row_content = [set() for i in range(M)]
        col_content = [set() for i in range(M)]
        box_content = [set() for i in range(M)]


        for i in range(M):
            for j in range(M):
                val = board[i][j]
                row_content[i].add(val)
                col_content[j].add(val)
                row_box, col_box = i // 3, j // 3
                box_pos = row_box * 3 + col_box
                box_content[box_pos].add(val)

        solved = False
        def populate(row, col):
            nonlocal solved
            
            if row == 9:
                solved = True
                return 
            next_row = row + (col + 1) // 9
            next_col = (col + 1) % 9
            if board[row][col] != '.':
                populate(next_row, next_col)
            else:
                row_box, col_box = row // 3, col // 3
                box_pos = row_box * 3 + col_box

                for i in range(ord('1'), ord('9') + 1):
                    current = chr(i)
                    if current not in row_content[row] and current not in col_content[col] and current not in box_content[box_pos]:
                        row_content[row].add(current)
                        col_content[col].add(current)
                        box_content[box_pos].add(current)
                        board[row][col] = current 
                        
                        populate(next_row, next_col)
                        if not solved:
                            row_content[row].remove(current)
                            col_content[col].remove(current)
                            box_content[box_pos].remove(current)
                            board[row][col] = '.'

        populate(0,0)