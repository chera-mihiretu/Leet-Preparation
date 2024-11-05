from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n, m = [int(i) for i in input().split()]  

    grid = [[0 for i in range(m)] for i in range(n)]

    for i in range(n):
        for j in range(m):
            current = 0
            if i % 2 == 0:
                if j % 2 == 0:
                    current = 1
            if i % 2 != 0:
                if j % 2 != 0:
                    current = 1
            grid[i][j] = current

                
    for row in grid:
        print(* row)


    


# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()