def prefix_sum(a):
	n = len(a)
	dp = [0] * (n+1)
	for i in range(1, n+1):
		dp[i] = dp[i-1] + a[i]
	return dp