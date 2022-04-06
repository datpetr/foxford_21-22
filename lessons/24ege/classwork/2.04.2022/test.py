def correct(ip):
	for i in ip:
		if int(i) <= 0 or int(i) >= 256:
			return False
	return True


f = open('files/24_7.txt', 'r').read().splitlines()
count = 0

for i in f:
	ip = i.split('.')
	if not('' in ip) and len(ip) == 4:
		if correct(ip):
			count += 1

print(count)
