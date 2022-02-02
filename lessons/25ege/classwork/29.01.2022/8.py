def sl(n):
	d = []
	for i in range (2, int(n ** 0.5) + 1):
		if n % i == 0:
			if i ** 2 != n:
				d.append(i)
				d.append(n // i)
			else:
				d.append(i)
	d.sort()
	return d


x = 10000001
k = 0

while k < 5:
	d = sl(x)
	if len(d) >= 2:
		s = d[-1] + d[-2]
		if s < 100000 and s % 1000 == 112:
			print(x, s)
			k += 1
	x += 1
