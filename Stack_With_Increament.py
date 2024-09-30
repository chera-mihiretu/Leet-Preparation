from typing import *

class CustomStack:
    def __init__(self, max_size: int):
        self._stack = [0] * max_size
        self._inc = [0] * max_size
        self._top = -1

    def push(self, x: int) -> None:
        if self._top < len(self._stack) - 1:
            self._top += 1
            self._stack[self._top] = x

    def pop(self) -> int:
        if self._top < 0:
            return -1

        result = self._stack[self._top] + self._inc[self._top]

        if self._top > 0:
            self._inc[self._top - 1] += self._inc[self._top]

        self._inc[self._top] = 0
        self._top -= 1
        return result

    def increment(self, k: int, val: int) -> None:
        if self._top >= 0:
            index = min(self._top, k - 1)
            self._inc[index] += val