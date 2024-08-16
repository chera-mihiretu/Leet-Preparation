if __name__ == '__main__':
    my_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        my_list.append([name, score])
    my_list.sort(key=lambda x: [x[1], x[0]])
    
    first = True
    num = my_list[0][1]
    answer = []
    for i in range(len(my_list)):
        if first:
            if num != my_list[i][1]:
                first = False
            num = my_list[i][1]
        else:
            if num != my_list[i][1]:
                break
        if not first:
            answer.append(my_list[i][0])
    print(*answer, sep='\n')
                
            