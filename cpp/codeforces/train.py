from sys import stdin 

input = lambda : stdin.readline().strip()

t = int(input())

for i in range(t):
    numbers = int(input())
    intervals = []
    for i in range(numbers):
        intervals.append([int(i) for i in input().split()])
    intervals.sort(key=lambda x: x[0])
    
    print(intervals)
