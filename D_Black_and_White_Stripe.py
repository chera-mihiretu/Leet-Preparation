from sys import stdin,stdout
from collections import Counter
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n, k = [int(i) for i in input().split()]
    string = input()

    count = Counter()
    answer = float('inf')
    for i in range(n):
        count[string[i]] += 1

        if (i+1)  >=  k:
            answer = min(count['W'], answer)
            count[string[i+1-k]] -= 1
    print(answer)


# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()