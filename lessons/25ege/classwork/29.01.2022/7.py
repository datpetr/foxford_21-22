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


x = 20000001
k = 0
s = 0

while k < 5:
	d = sl(x)
	if len(d) >= 5:
		for i in range(5):
			s *= d[i]
		# s = d[0] * d[1] * d[2] * d[3] * d[4]
		if s < x and s % 10 == 1:
			print(x, s, d[4])
			k += 1
		s = 1
	x += 1
