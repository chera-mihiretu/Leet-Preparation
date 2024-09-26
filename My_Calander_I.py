from typing import *

class MyCalendar:
    """
    [a,b], [c, d]

    a <= x 
    [x, y]
    """
    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> bool:
        index = bisect_right(self.events, [start, end])
        if index - 1 >= 0:
            if start < self.events[index - 1][1]:
                return False
        if index < len(self.events):
            if end > self.events[index][0] :
                return False
        
        self.events.insert(index, [start, end])
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)