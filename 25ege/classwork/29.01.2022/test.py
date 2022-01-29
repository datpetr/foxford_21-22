def simple(n):
	for i in range (2, int(n ** 0.5) + 1):
		if n % i == 0:
			return False
	return True


mx = 0


for num in range(500000, 900001):
	d = []
	for i in range(2, int(num ** 0.5) + 1):
		if num % i == 0:
			if i != num // i:
				if simple(i):
					d.append(i)
				if simple(num // i):
					d.append(i)
			else:
				if simple(i):
					d.append(i)
	if len(d) == 7:
		print(num, max(d))
