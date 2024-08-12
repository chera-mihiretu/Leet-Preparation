from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    string = input()
    key_index = {c:i for i , c in enumerate(string) }
    toType = input()
    cur = toType[0]
    answer = 0
    
    for i in range(len(toType)):
        answer += (abs(key_index[toType[i]] - key_index[cur]))
        cur = toType[i]
    print(answer)


# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()