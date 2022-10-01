def base_converter(n, k):
	s = ''
	while n > 0:
		if n % k < 10:
			s += str(n % k)
		else:
			s += chr(n % k - 10 + ord('A'))
		n //= k
	return s[::-1]