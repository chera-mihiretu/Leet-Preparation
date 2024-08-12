from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    length = int(input())
    nums = [int(i) for i in input().split()]
    even = []
    odd = []
    for i in range(length):
        if nums[i] & 1:
            odd.append(nums[i])
        else:
            even.append(nums[i])
    even.sort(reverse=True)
    odd.sort(reverse=True)
    pointer1 = 0
    pointer2 = 0
    aliceTurn = True
    score = [0,0] # alice, bob
    while pointer1 < len(even) and pointer2 < len(odd):
        if aliceTurn:
            if even[pointer1] > odd[pointer2]:
                score[0] += even[pointer1]
                pointer1 += 1
            else:
                pointer2 += 1
            aliceTurn = False
        else:
            if odd[pointer2] > even[pointer1]:
                score[1] += odd[pointer2]
                pointer2 += 1
            else:
                pointer1 += 1 
            aliceTurn = True
    if pointer1 < len(even):
        if not aliceTurn:
            pointer1 += 1
        while pointer1 < len(even):
            score[0] += even[pointer1]
            pointer1 += 2
    if pointer2 < len(odd):
        if aliceTurn:
            pointer2 += 1
        while pointer2 < len(odd):
            score[1] += odd[pointer2]
            pointer2 += 2
    #print(score)
    if score[0] > score[1]:
        print('Alice')
    elif score[0] < score[1]:
        print('Bob')
    else:
        print('Tie')

# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()