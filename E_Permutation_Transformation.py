
import sys, threading

input = lambda: sys.stdin.readline().strip()

def solve():
    n = int(input())

    nums = [int(i) for i in input().split()]
    answer = [0 for i in range(n)]

    def formTree(left, right, depth):
        if left > right:
            return 
        index = left
        for i in range(left, right + 1):
            if nums[index] < nums[i]:
                index = i

        answer[index] = depth

        
        formTree(left, index - 1, depth=depth + 1)
        formTree(index + 1, right, depth=depth + 1)
    formTree(0, len(nums) - 1 ,0)

    print(*answer)
            


def main():
    test = int(input())

    for i in range(test):
        solve()
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
