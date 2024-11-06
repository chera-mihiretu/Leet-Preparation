from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n, m = [int(i) for i in input().split()]  

    grid = [[0 for i in range(m)] for i in range(n)]

    grid[0][0] = 1

        


    


# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()