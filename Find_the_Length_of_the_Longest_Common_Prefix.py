from typing import *

class Trie:
    def __init__(self):
        self.children = [None for i  in range(10)]
    
    def countCommon(self, word):
        
        count = 0
        current = self
        for i in word:
            index = int(i)
            if current.children[index]:
                count += 1
                current = current.children[index]
            else:
                break
        return count
    def buildWord(self, word):
        current = self
        for i in word:
            index = int(i)
            if not current.children[index]:
                current.children[index] = Trie()
            current = current.children[index]



    
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        myTrie = Trie()
        for i in arr2:
            myTrie.buildWord(str(i))
        answer = 0
        for i in arr1:
            answer = max(answer, myTrie.countCommon(str(i)))
        return answer


    

        