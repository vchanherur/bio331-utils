# Here's a testing file for the graph and file tools.

from file_tools import *
from graph_tools import *

# testing readin
n,e,w = readin("test.txt",True)

# testing adj_list:
print("adjlist: ",adj_list(n,e))

# testing node_degree (in,out,both) with s = b
print("indegree: ",node_degree("b",n,e,"in"))
print("outdegree: ",node_degree("b",n,e,"out"))
print("totaldegree: ",node_degree("b",n,e))

# testing bfs
print("bfs: ",bfs(n,e,"a"))

# testing lcc
print("lcc: ",lcc(n,e))

# testing random node
print("random node: ",random_node(n))

# testing random edge
print("random edge: ",random_edge(e))
