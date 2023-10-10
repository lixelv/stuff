with open('27-A.txt', 'r') as f:
	lst = [k.split('  ') for k in f.read().split('\n')]
	even_odd = 0
	for k in range(len(lst)):
		lst[k][0], lst[k][1] = int(lst[k][0]), int(lst[k][1])
		if lst[k][1] > lst[k][0]:
			lst[k][0], lst[k][1] = lst[k][1], lst[k][0]
		even_odd += 1 if lst[k][0] % 2 == 0 else -1
	if even_odd >= 0:
		even_odd = 0
	else:
		even_odd = 1
	s = 0
	for k in range(len(lst)):
		s += lst[k][0] if lst[k][0] % 2 == even_odd else lst[k][1]
		print(lst[k][0] if lst[k][0] % 2 == even_odd else lst[k][1])
	print(s)