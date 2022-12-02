global a, visited
a = []
visited = [0] * len(a)

# directed graph cycle
def dfs(u):
	visited[u] = -1

	for v in a[u]:
		if visited[v] == -1:
			return True
		if not visited[v] and dfs(v):
			return True

	visited[u] = 1
	return False


# undirected graph cycle
def dfs(u, parent):
	visited[u] = True

	for v in a[u]:
		if visited[v] and v != parent:
			return True
		if not visited[v] and dfs(v, u):
			return True

	return False