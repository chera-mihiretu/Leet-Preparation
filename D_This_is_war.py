from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    length = int(input())
    nums = [int(i) for i in input().split()]
    nums = [[nums[i], i] for i in range(length)]
    nums.sort()
    answer = [True for i in range(length)]
    counter = nums[0][0]
    for i in range(1, length):
        if counter < nums[i][0]:
            answer[i-1] = False
        counter += nums[i][0]
    pre = True
    final_answer = []
    for i in range(length - 1, -1, -1):
        if answer[i] == False:
            break
        final_answer.append(nums[i][1] + 1)
    final_answer.sort()
    print(len(final_answer))
    print(*final_answer)


        



# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()