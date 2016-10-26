# Here's a testing file for the graph and file tools.

from file_tools import *
from graph_tools import *

# testing readin
n,e,w = readin("test.txt",True)

# testing adj_list:
print(adj_list(n,e))

# testing node_degree (in,out,both) with s = b
print(node_degree("b",n,e,"in"))
print(node_degree("b",n,e,"out"))
print(node_degree("b",n,e))

# testing bfs
print(bfs(n,e,"A"))

# testing lcc
print(lcc(n,e))

# testing random node
print(random_node(n))

# testing random edge
print(random_edge(e))
