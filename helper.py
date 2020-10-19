descrepition='''
Plot a directed graph through the edge file and node file,you can set it to be undirected by use "-u" or "--undirected" parameter.
The node file is not necessary while nodes on your graph are simple
See the help information of the corresponding parameter for details.
'''

nodes_help = '''
The file contains all vertices in graph with attributes, and it should be a csv file.
It's not necessary while nodes have simple attributes only (just have node names). 
 '''

edges_help='''
The file contains all edges in graph without self-loop, it should be a csv file, and default is "./edges.csv".
If there are some single node in graph, use the same "source" and "target" to plot it.
'''

output_help='''
The output html file, default is "SimplePlot.html".
'''

undirect_help='''
Global option of edge's direction, the graph is directed in default, use it to set the graph to be undircted.
'''
