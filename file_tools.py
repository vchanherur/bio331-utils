# File functions

def readin(file,directed=False):
	# reads in a file of the format:
	# node1\tnode2\tweight
	# returns a list of nodes, dict of tuples of edges,
	# and dict of weights if they exist.
	# If directed, pass in True as 2nd arg.

	n = [] # node list
	e = [] # edge list
	w = {} # weight dict

	f = open(file)

	# make list of nodes
	for line in f:
		nnew = line.rstrip("\n").split("\t")
		if nnew[0] not in n and nnew[1] not in n:
			n.append(nnew[0])
			n.append(nnew[1])
		elif nnew[0] not in n:
			n.append(nnew[0])
		elif nnew[1] not in n:
			n.append(nnew[1])
	
	# make dict of edges
	f.seek(0)
	for line in f:
		enew = line.rstrip("\n").split("\t")
		if enew[0] == enew[1]: # ignore self-loops
			pass
		if enew[:2] in e: # ignore exact repeat
			pass
		if tuple((enew[1],enew[0])) in e and not directed: # ignores direction
			pass			      # if undirected
		else:
			e.append(tuple(enew[:2])) # stores edge
			w[tuple(enew[:2])] = enew[2] # stores weight

	f.close()

	return n,e,w
