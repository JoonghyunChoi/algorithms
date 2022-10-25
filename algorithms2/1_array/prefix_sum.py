def prefix_sum(a):
	n = len(a)
	p = [0] * (n+1)

	for i in range(1, n+1):
		p[i] = p[i-1] + a[i]
	return p