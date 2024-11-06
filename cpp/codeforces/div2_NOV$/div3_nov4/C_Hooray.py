from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n,m  = [int(i) for i in input().split()]
    answer = [0 for i in range(n)]
    pref = [0 for i in range(n)]

    query = []
    for i in range(m):
        query.append([int(i) for i in input().split()])

    for i in range(m - 1, -1, -1):
        fr, to, winer = query[i]

        



# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        solution()