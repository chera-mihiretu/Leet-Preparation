def find_group(x, group):
    if x == group[x]:
        return x
    group[x] = find_group(group[x], group)
    return group[x]

def merge_group(a, b, group):
    a = find_group(a, group)
    b = find_group(b, group)
    if a != b:
        group[a] = b

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    N = int(data[index])
    index += 1

    group = list(range(N + 1))
    P = [0] * (N + 1)
    S = [""] * (N + 1)

    for i in range(1, N + 1):
        P[i] = int(data[index])
        index += 1

    for i in range(1, N + 1):
        S[i] = data[index]
        index += 1
        for j in range(1, N + 1):
            if S[i][j - 1] == '1':
                merge_group(i, j, group)

    pos = [[] for _ in range(N + 1)]
    cnt = [0] * (N + 1)

    for i in range(1, N + 1):
        g = find_group(i, group)
        pos[g].append(P[i])
    
    for i in range(1, N + 1):
        pos[i].sort()

    result = []
    for i in range(1, N + 1):
        g = find_group(i, group)
        result.append(pos[g][cnt[g]])
        cnt[g] += 1

    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
