from collections import deque
MAXN = 1000005

v = [[] for i in range(MAXN)]

def add_edge(a, b, fre):
	v[a].append(b)
	fre[b] += 1

def topological_sorting(fre, n):
	q = deque()

	for i in range(n):
		if (not fre[i]):
			q.append(i)

	l = []

	while (len(q) > 0):
		u = q.popleft()

		l.append(u)

		for i in range(len(v[u])):
			fre[v[u][i]] -= 1

			if (not fre[v[u][i]]):
				q.append(v[u][i])
	return l

def numberofPaths(source, destination, n, fre):

	s = topological_sorting(fre, n)

	dp = [0]*n

	dp[destination] = 1

	for i in range(len(s) - 1,-1,-1):
		for j in range(len(v[s[i]])):
			dp[s[i]] += dp[v[s[i]][j]]
	return dp

if __name__ == '__main__':

	n = 5
	source, destination = 0, 4

	fre = [0]*n

	add_edge(0, 1, fre)
	add_edge(0, 2, fre)
	add_edge(0, 3, fre)
	add_edge(0, 4, fre)
	add_edge(2, 3, fre)
	add_edge(3, 4, fre)

	print (numberofPaths(source, destination, n, fre))
