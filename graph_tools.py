# Graph tools

from collections import deque

def adj_list(n,e):
	# given a list of nodes and dict of list of edges,
	# return an adjacency list as a dict.

	adl = {i:[] for i in n}

	for edge in e:
		if edge[1] not in adl[edge[0]]:
			adl[edge[0]].append(edge[1])
		if edge[0] not in adl[edge[1]]:
			adl[edge[1]].append(edge[0])
	
	return adl

def node_degree(s,n,e,which="both"):
	# given a list of nodes and dict of list of edges,
	# and a node s, find the degree of the node, "in", "out"
	# or "both" (default) degree.

	ind = 0
	oud = 0

	for edge in e:
		source = edge[0]
		target = edge[1]
		if s == source: # outdeg
			oud += 1
		if s == target: # indeg
			ind += 1
	
	if which == "in":
		return ind
	elif which == "out":
		return oud
	else: 
		return ind+oud

def bfs(n,e,s):
	# given a list of nodes and dict of list of edges,
	# and a node s, find the distance of each node to s,
	# return the nodes in the connected component.

	Q = deque([]) # empty queue
	visited = []

	visited.append(s)
	Q.append(s)

	# make adj. list
	N = adj_list(n,e)

	while Q:
		w = Q.popleft() # dequeue
		for neighbor in N[w]:
			if neighbor not in visited:
				visited.append(neighbor)
				Q.append(neighbor)

	return visited

def lcc(n,e):
	# given a list of nodes and dict of list of edges,
	# find the largest connected component and return its nodes.

	visited = []
	notV = [i for i in V]

	largestCCv = [] # nodes in largest cc

	while notV:
		cc = bfs(n,e,notV[0])
		for i in notV:
			notV.remove(i)
		if len(cc) > len(largestCCv):
			largestCCv = [i for i in cc]
	largestCCe = edgesubset(largestCCv,e)

	return largestCCv,largestCCe

	
def edgesubset(n,e):
	# given a list of nodes and edges, returns subset of edges
	# that only are made up of nodes in n.

	edges = []

	for edge in e:
		if edge[0] in n and edge[1] in n:
			edges.append(e)
	
	return edges

def random_edge(e):
	# given a list of edges, return a random edge.
	return random.choice(e.keys())

def random_node(n):
	# given a list of nodes, return a random node.
	return random.choice(n)
