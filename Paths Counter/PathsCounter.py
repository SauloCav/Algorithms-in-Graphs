# Python3 program for Number of paths
# from one vertex to another vertex
# in a Directed Acyclic Graph
from collections import deque
MAXN = 1000005

# to make graph
v = [[] for i in range(MAXN)]

# function to add edge in graph
def add_edge(a, b, fre):

	# there is path from a to b.
	v[a].append(b)
	fre[b] += 1

# function to make topological sorting
def topological_sorting(fre, n):
	q = deque()

	# insert all vertices which
	# don't have any parent.
	for i in range(n):
		if (not fre[i]):
			q.append(i)

	l = []

	# using kahn's algorithm
	# for topological sorting
	while (len(q) > 0):
		u = q.popleft()
		#q.pop()

		# insert front element of queue to vector
		l.append(u)

		# go through all it's childs
		for i in range(len(v[u])):
			fre[v[u][i]] -= 1

			# whenever the frequency is zero then add
			# this vertex to queue.
			if (not fre[v[u][i]]):
				q.append(v[u][i])
	return l

# Function that returns the number of paths
def numberofPaths(source, destination, n, fre):

# make topological sorting
	s = topological_sorting(fre, n)

	# to store required answer.
	dp = [0]*n

	# answer from destination
	# to destination is 1.
	dp[destination] = 1

	# traverse in reverse order
	for i in range(len(s) - 1,-1,-1):
		for j in range(len(v[s[i]])):
			dp[s[i]] += dp[v[s[i]][j]]
	return dp

# Driver code
if __name__ == '__main__':

	# here vertices are numbered from 0 to n-1.
	n = 5
	source, destination = 0, 4

	# to count number of vertex which don't
	# have any parents.
	fre = [0]*n

	# to add all edges of graph
	add_edge(0, 1, fre)
	add_edge(0, 2, fre)
	add_edge(0, 3, fre)
	add_edge(0, 4, fre)
	add_edge(2, 3, fre)
	add_edge(3, 4, fre)

	# Function that returns the number of paths
	print (numberofPaths(source, destination, n, fre))

# This code is contributed by mohit kumar 29.
