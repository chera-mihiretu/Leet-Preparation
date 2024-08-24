from sys import stdin, stdout

def input():
    return stdin.readline().strip()

################################################
def main():
    n = int(input())
    array = list(map(int, input().split()))
    count = 0
    def devide(start, end):
        nonlocal count
        mid = start + (end - start) // 2
        if end - start == 0:
            return 0
        if end - start == 1:
            if array[start] > array[end]:
                array[start], array[end] = array[end],array[start]
                count += 1
            return array[start] + array[end]    

        left = devide (start, mid)
        right = devide (mid + 1,end)
        
        if left > right:
            array[start:mid+1], array[mid+1:end+1] = array[mid+1:end+1], array[start:mid+1]
            count += 1
        return left + right
        
    devide(0, n-1)
    for i in range(1, len(array)):
        if array[i] < array[i-1]:
            print(-1)
            break
    else:
        print(count)


################################################


if __name__ == '__main__':
    test = int(input())
    for i in range(test):
        main()
