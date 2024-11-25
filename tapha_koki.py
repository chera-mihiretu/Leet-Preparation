
ss = lambda x,y: x - y
dd = lambda x,y:  x/y if (y != 0)  else -100000
mm = lambda x,y: x * y
aa = lambda x,y: x + y

answer = []
def recursion(used, total, cur):
	print(total)
	if used == 3: 
		if total == 6:
			return True
		return False

	operator = [ss, dd, aa, mm]

	for i in range(len(operator)):
		
		value = recursion(used + 1, operator[i](total, cur), cur)
		if value:
			answer.append(i)
			return True
	return False
result = []
for i in range(2, 10):
	answer.append(f'Number {i}')
	result.append(answer.copy())
	answer.clear()
	recursion(1, i, i)

print(result)


