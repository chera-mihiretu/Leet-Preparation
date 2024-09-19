from typing import *



def solution(string):
    pointer = start = 0
    wich_child = None
    stack = []
    
    while pointer < len(string):
        print(stack, pointer, start)
        if string[pointer] != ']':
            start = pointer + 2
            while string[pointer] != ',':
                pointer += 1
            stack.append(string[start:pointer])
            pointer += 1
        else:
            stack.pop()
            pointer += 1
    

            


if __name__ == '__main__':
    solution('R[3,L[4,]R[123,]]')