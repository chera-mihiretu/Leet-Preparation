from sys import stdin , stdout 

input = lambda : stdin.readline().strip()
def pp(x):
    stdout.write(f'{x}\n')
    stdout.flush()
ww = lambda x : pp(x)

def solve():
    answer = []
    def divide(start, end):
        if start > end: return 
        if start == end:
            answer.append(start)
            return 
        
        mid = start + (end - start) // 2

        ww(f"xor {start} {mid}")
        left = int(input())
        ww(f"xor {mid + 1} {end}")
        right = int(input())

        if right: divide(mid + 1, end)
        if left: divide(start, mid)
    n = int(input())

    divide(1, n)

    print(f"ans", *answer)

t = int(input())

for i in range(t):
    solve()
