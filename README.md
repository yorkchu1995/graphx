Graphx
========
Graphx is a Python package for the creation, manipulation,and study of the structure, dynamics, and functions of Graph,also can be used for complex networks.


Install
----

Install the latest version of Graphx:

    $ pip install graphx

Install with all optional dependencies:

    $ pip install graphx[all]
Simple example
--------------

Create a new structure of graph, which is based on adjacent matrix:

    >>> import graphx as gx
    >>> g = gx.Graph()
    >>> g.insert_node()
    >>> g.insert_node()
    >>> g.add_edge(0, 1, directed=0)
    >>> g.adj_mat
    
More
-------

For more details, please see `example.html`,whose dataset is on the directory `data`.