from typing import *
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_count = set(allowed)
        count = 0
        for word in words:
            current_count= set(word)
            if current_count | allowed_count == allowed_count:
                
                count += 1
        return count