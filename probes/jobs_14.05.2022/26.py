# ip = '174.23.88.201'
# mask = '255.255.192.0'
# ip_oct = int(''.join([f'{int(x):08b}' for x in ip.split('.')]), 2)
# mask_oct = int(''.join([f'{int(x):08b}' for x in mask.split('.')]), 2)
#
# print(f'{ip_oct&~mask_oct:032b}')
mask = '255.255.224.0'
mask_oct = [int(x) for x in mask.split('.')]

f = open('files/26.txt')
n = int(f.readline())
req = {}

for _ in range(n):
    ip_oct = list(map(int, f.readline().split()))
    net = tuple(i & m for i, m in zip(ip_oct, mask_oct))
    node = tuple(i & ~m for i, m in zip(ip_oct, mask_oct))
    if net in req:
        req[net][0] += 1
        req[net][1].add(node)
    else:
        req[net] = [1, {node}]

s = min((-v[0], -len(v[1]), i) for i, v in req.items())
print('.'.join(map(str, s[2])), s[0])
