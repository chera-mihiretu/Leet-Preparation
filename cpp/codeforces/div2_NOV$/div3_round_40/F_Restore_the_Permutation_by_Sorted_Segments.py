from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n = int(input())
    array = []
    for _ in range(n-1):
        row = [int(i) for i in input().split()][1:]
        
        
        array.append(set(row))
    print(array)

# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()