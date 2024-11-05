from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n,m  = [int(i) for i in input().split()]
    answer = [0 for i in range(n)]
    for _ in range(m):
        li, ri , xi = [int(i) for i in input().split()]

        if xi == ri:
            answer[li - 1] = xi
        if xi == li:
            answer[ri - 1] = xi
    print(*answer)

# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        solution()