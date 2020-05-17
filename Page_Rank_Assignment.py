import networkx as nx



#Implemented Google's First Page Rank Algorithm
class digraph(nx.DiGraph) :
#custom directed graph
class DGraph:
    #Directed graph is represented by an adjacency matrix
    def __init__(self, n, e):
        self.n = n #number of nodes
        self.m = [[0] * n for _ in range(n)] #adjacency matrix
        self.add_edges(e)

    def add_edges(self, e):
        for f,t in e:
            self.m[f][t] = 1

    def pagerank(self, iterations):
        M = self.m
        temp = [0] * len(M)
        # print(temp)
        for i in range(len(M)):
            if M[i] == temp:
                M[i] = [1] * len(M)
                M[i][i] = 0

        L = [0] * len(M)
        i = 0
        for sa in M:
            L[i] += (sum(s for s in sa))
            i += 1
        V = [1 / len(M)] * len(M)

        for i in range(iterations):
            new = [0] * len(M)
            for v in range(len(M)):
                for j in range(len(M[v])):
                    if M[v][j] == 1:
                        new[j] += 0.85 * (V[v] / L[v])
            V = new
            for i in range(len(V)):
                V[i] += (0.15) / len(M)
        #change the answer V to dictionary so it is easier to compare with NetworkX solution
        dV = dict()
        j = 0
        for i in V:
            dV[j] = i
            j += 1
        return dV
#test with wikipedia picture. Same numbers as the
def wiki():
    e = [(1,2),(2,1),(3,0),(3,1),(4,3),(4,1),(4,5),(5,1),(5,4),(6,1),(6,4),(7,1),(7,4),(8,1),(8,4),(9,4),(10,4)]
    myGraph = DGraph(11, e)
    myRank = myGraph.pagerank(100)
    print('Wikipedia example:')
    print(myRank)

#tester with 200 nodes
def g1():
    er = nx.gnm_random_graph(200, 400, seed=None, directed=True)
    myGraph = DGraph(200,er.edges)
    myRanks = myGraph.pagerank(100)
    print('My Ranks (200 Nodes):', myRanks)
    print('NetworkX Ranks (200 Nodes):',nx.pagerank(er))

#tester with 400 nodes
def g2():
    er = nx.gnm_random_graph(400, 800, seed=None, directed=True)
    myGraph = DGraph(400,er.edges)
    myRanks = myGraph.pagerank(100)
    print('My Ranks (400 Nodes):', myRanks)
    print('NetworkX Ranks (400 Nodes):',nx.pagerank(er))

#tester with 600 nodes
def g3():
    er = nx.gnm_random_graph(600, 1000, seed=None, directed=True)
    myGraph = DGraph(600,er.edges)
    myRanks = myGraph.pagerank(100)
    print('My Ranks (600 Nodes):', myRanks)
    print('NetworkX Ranks (600 Nodes):',nx.pagerank(er))

#tester with 1000 nodes
def g4():
    er = nx.gnm_random_graph(1000, 1800, seed=None, directed=True)
    myGraph = DGraph(1000,er.edges)
    myRanks = myGraph.pagerank(100)
    print('My Ranks (1000 Nodes):', myRanks)
    print('NetworkX Ranks (1000 Nodes):',nx.pagerank(er))

wiki()
g1()
g2()
g3()
g4()
