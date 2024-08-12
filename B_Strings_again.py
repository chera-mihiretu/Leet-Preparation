from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n,m,k = [int(i) for i in input().split()]
    a = list(input())
    b = list(input())
    a.sort(reverse=True)
    b.sort(reverse=True)
    from_who = [0,0] # a, b
    c = []
    while a and b:
        if a[-1] < b[-1]:
            if from_who[0] < k:
                c.append(a.pop())
                from_who[0] += 1
                from_who[1] = 0
            else:
                c.append(b.pop())
                from_who[0] = 0
                from_who[1] +=1
        else:
            if from_who[1] < k:
                c.append(b.pop())
                from_who[0] = 0
                from_who[1] += 1
            else:
                c.append(a.pop())
                from_who[0] += 1
                from_who[1] = 0
    print(''.join(c))
        

    


# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()