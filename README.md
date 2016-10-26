# bio331-utils
Utility functions for Reed College Bio331: Computational Systems Biology. 

Vikram's version of the utilities, updated, a second time.

## QuickStart

These utility functions are used in Bio331, starting with Lab1.  They are wrapper scripts to post graphs to [GraphSpace@Reed](http://ec2-52-41-252-78.us-west-2.compute.amazonaws.com/), a web server for interactive graph sharing and collaboration.

- `json_utils.py` contains functions to write an annotated graph to a text file in [JSON](http://www.json.org/) format readable by GraphSpace.
- `graphspace_utils.py` contains [curl commands](https://curl.haxx.se/docs/manpage.html) to post the JSON file to GraphSpace.
- `file_tools.py` contains a function to read in a graph represented as a tsv: `node1``\t``node2``\t``weight(optional)`, such as `test.txt`.
- `graph_tools.py` contains several functions to:
-- compute an adjacency list,
-- find a node degree,
-- run a breadth-first search,
-- find the largest connected component,
-- choose a random edge, and
-- choose a random node.

Auto-generated documentation is available on the [Bio331 website](http://www.reed.edu/biology/courses/bio331/) under [Support Code](http://www.reed.edu/biology/courses/bio331/supportcode/index).

## GraphSpace

GraphSpace was originally developed at Virginia Tech.  It is available at (www.graphspace.org) and the source code is available on the [GitHub Page](https://github.com/Murali-group/GraphSpace).
