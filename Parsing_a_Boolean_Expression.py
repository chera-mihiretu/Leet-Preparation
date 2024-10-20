from typing import *

class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []

        # for converting t -> True and f -> False vice versa
        self.hash = {'f':False, 't':True}
        self.revHash = {False: 'f', True: 't'}
        # starting the the iteration from back 
        for i in range(len(expression) - 1, -1, -1):

            value = None
            while stack and expression[i] in {'|', '&', '!'}:
                # to begin with current expression that is after (
                if value == None:
                    value = self.hash[stack[-2]]
                current = stack.pop()

                # breaking the while loop whenever we face )
                if current == ')':
                    stack.append(self.revHash[value])
                    break


                value = self.orAndOperation(stack[-1], value, expression[i])


            else:
                # we only need this when the while is not executed
                stack.append(expression[i])
        
        return self.hash[stack[0]]

    # to evaluate the current value of expression 
    def orAndOperation(self, current, value, expression):
        if current == 'f' or current == 't':
            if expression == '|':
                value |= self.hash[current]
            elif expression == '&':
                value &= self.hash[current]
            else:
                value = not value 
        return value

            

