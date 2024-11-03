from sortedcontainers import SortedSet
from sys import stdin 

input = lambda : stdin.readline().strip()

def solution():
    n = int(input())
    array  =[]
    for _  in range(n):
        array.append([int(i) for i in input().split()])

    array.sort()
    answer = 0
    sorted_set = SortedSet()
    # print(array)
    for fr, to in array:
        current = (len(sorted_set)) -  sorted_set.bisect_left(to)
        answer += current
        sorted_set.add(to)

    print(answer)

if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()
