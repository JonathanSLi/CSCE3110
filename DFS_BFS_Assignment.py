import networkx as nx
import networkx.algorithms.traversal.depth_first_search as algs
import networkx.algorithms.traversal.breadth_first_search as algbfs





  def rand(self):
    er = nx.dense_gnm_random_graph(24, 27)
    for e in er.edges() :
      f,t=e
      self.add_edge(f,t)
    er = nx.dense_gnm_random_graph(24, 7)
    for e in er.edges() :
      f,t=e
      self.add_edge(t,f)

    return self

#DFS edges
def df_edges(g,source):
  visited=set()
  def visit(node) :
    if node in visited : return
    visited.add(node)
    for child in g[node] :
      if child not in visited:
        yield (node, child)
      for edge in visit(child) :
        yield edge
  for n in visit(source) :
    yield n

#BFS iterate through nodes
def bf_nodes(g,source):
    visited = set()
    q = []
    q.append(source)
    visited.add(source)
    while q:
        s = q.pop(0)
        yield s
        for i in g[s]:
            if i not in visited:
                q.append(i)
                visited.add(i)

#tester, runs random graph and prints networkx and my solution
def t1() :
    g=digraph().rand()
    ns= list(algs.dfs_edges(g,source=0))
    print("NetworkX DFS Edges: ", ns)
    print("My DFS Edges:       ", list(df_edges(g,0)))
    ds = [0] + list(map(lambda b: b[1], algbfs.bfs_edges(g,source=0)))
    print("NetworkX BFS Edges: ", ds)
    print("My BFS Edges:       ", list(bf_nodes(g,0)))

#iterates through t1
def t2():
    for i in range(10):
        print('TEST ', i+1)
        t1()
        print()
'''
TEST  1
NetworkX DFS Edges:  [(0, 14), (0, 17), (17, 23), (0, 22), (22, 21)]
My DFS Edges:        [(0, 14), (0, 17), (17, 23), (0, 22), (22, 21)]
NetworkX BFS Edges:  [0, 14, 17, 22, 23, 21]
My BFS Edges:        [0, 14, 17, 22, 23, 21]

TEST  2
NetworkX DFS Edges:  [(0, 12), (12, 20), (20, 7), (7, 17), (17, 18), (17, 10), (7, 19)]
My DFS Edges:        [(0, 12), (12, 20), (20, 7), (7, 17), (17, 18), (17, 10), (7, 19)]
NetworkX BFS Edges:  [0, 12, 20, 7, 17, 19, 18, 10]
My BFS Edges:        [0, 12, 20, 7, 17, 19, 18, 10]

TEST  3
NetworkX DFS Edges:  [(0, 11), (11, 13), (13, 22), (11, 20), (20, 23), (23, 19), (11, 5), (5, 7), (7, 10), (10, 6), (6, 14), (14, 17)]
My DFS Edges:        [(0, 11), (11, 13), (13, 22), (11, 20), (20, 23), (23, 19), (11, 5), (5, 7), (7, 10), (10, 6), (6, 14), (14, 17)]
NetworkX BFS Edges:  [0, 11, 13, 20, 5, 22, 23, 7, 19, 10, 6, 14, 17]
My BFS Edges:        [0, 11, 13, 20, 5, 22, 23, 7, 19, 10, 6, 14, 17]

TEST  4
NetworkX DFS Edges:  [(0, 3), (3, 21), (21, 18), (0, 7), (7, 8), (8, 9), (9, 15), (15, 19), (15, 11), (11, 12), (12, 20), (11, 13), (13, 17), (17, 22), (22, 23), (11, 14), (7, 6)]
My DFS Edges:        [(0, 3), (3, 21), (21, 18), (0, 7), (7, 8), (8, 9), (9, 15), (15, 19), (15, 11), (11, 12), (12, 20), (11, 13), (13, 17), (17, 22), (22, 23), (11, 14), (7, 6)]
NetworkX BFS Edges:  [0, 3, 7, 21, 8, 11, 15, 6, 18, 9, 22, 12, 13, 14, 19, 23, 20, 17]
My BFS Edges:        [0, 3, 7, 21, 8, 11, 15, 6, 18, 9, 22, 12, 13, 14, 19, 23, 20, 17]

TEST  5
NetworkX DFS Edges:  [(0, 8)]
My DFS Edges:        [(0, 8)]
NetworkX BFS Edges:  [0, 8]
My BFS Edges:        [0, 8]

TEST  6
NetworkX DFS Edges:  [(0, 5), (5, 7), (7, 12), (12, 17), (7, 21), (21, 22), (21, 11), (11, 13), (13, 4), (4, 10), (10, 3)]
My DFS Edges:        [(0, 5), (5, 7), (7, 12), (12, 17), (7, 21), (21, 22), (21, 11), (11, 13), (13, 4), (4, 10), (10, 3)]
NetworkX BFS Edges:  [0, 5, 7, 12, 22, 4, 21, 17, 10, 11, 3, 13]
My BFS Edges:        [0, 5, 7, 12, 22, 4, 21, 17, 10, 11, 3, 13]

TEST  7
NetworkX DFS Edges:  [(0, 9), (9, 12), (12, 5), (5, 8), (5, 13), (13, 16), (13, 17), (17, 18), (18, 11), (11, 19), (19, 20), (19, 21), (19, 23), (19, 7), (7, 10), (19, 15), (11, 6)]
My DFS Edges:        [(0, 9), (9, 12), (12, 5), (5, 8), (5, 13), (13, 16), (13, 17), (17, 18), (18, 11), (11, 19), (19, 20), (19, 21), (19, 23), (19, 7), (7, 10), (19, 15), (11, 6)]
NetworkX BFS Edges:  [0, 9, 21, 12, 18, 5, 11, 8, 13, 19, 6, 16, 17, 20, 23, 7, 15, 10]
My BFS Edges:        [0, 9, 21, 12, 18, 5, 11, 8, 13, 19, 6, 16, 17, 20, 23, 7, 15, 10]

TEST  8
NetworkX DFS Edges:  [(0, 20), (20, 6), (6, 18), (18, 21)]
My DFS Edges:        [(0, 20), (20, 6), (6, 18), (18, 21)]
NetworkX BFS Edges:  [0, 20, 6, 18, 21]
My BFS Edges:        [0, 20, 6, 18, 21]

TEST  9
NetworkX DFS Edges:  [(0, 5), (5, 15), (15, 17), (17, 22), (15, 21), (21, 3), (3, 13), (13, 8), (8, 16), (16, 19), (8, 2), (2, 6), (21, 10), (10, 12), (21, 20)]
My DFS Edges:        [(0, 5), (5, 15), (15, 17), (17, 22), (15, 21), (21, 3), (3, 13), (13, 8), (8, 16), (16, 19), (8, 2), (2, 6), (21, 10), (10, 12), (21, 20)]
NetworkX BFS Edges:  [0, 5, 15, 20, 17, 21, 22, 3, 10, 13, 12, 19, 8, 16, 2, 6]
My BFS Edges:        [0, 5, 15, 20, 17, 21, 22, 3, 10, 13, 12, 19, 8, 16, 2, 6]

TEST  10
NetworkX DFS Edges:  [(0, 4), (4, 6), (6, 9), (9, 10), (10, 18), (10, 21), (21, 22), (22, 23), (21, 5), (5, 8), (8, 12), (8, 20), (9, 17), (6, 19)]
My DFS Edges:        [(0, 4), (4, 6), (6, 9), (9, 10), (10, 18), (10, 21), (21, 22), (22, 23), (21, 5), (5, 8), (8, 12), (8, 20), (9, 17), (6, 19)]
NetworkX BFS Edges:  [0, 4, 9, 22, 6, 10, 17, 23, 19, 18, 21, 5, 8, 12, 20]
My BFS Edges:        [0, 4, 9, 22, 6, 10, 17, 23, 19, 18, 21, 5, 8, 12, 20]
'''

