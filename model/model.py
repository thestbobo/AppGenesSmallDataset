import copy

import networkx as nx
from database.DAO import DAO

class Model:
    def __init__(self):
        self._myGraph = nx.DiGraph()
        self._chrMap = {}

        self._path_best = None
        self._weight_best = None


        pass


    def getPath(self, soglia):
        self._path_best = []
        self._weight_best = 0

        partial = []

        for n in self._myGraph.nodes:
            partial.append(n)
            self._recursion(partial, soglia)
            partial.pop()


        return self._path_best, self._weight_best

    def _recursion(self, partial, soglia):
        current_node = partial[-1]
        # terminazione
        if self._countValidNeighbors(current_node, soglia) == 0:
            if self._weight_best < self._getWeight(partial):
                self._weight_best = self._getWeight(partial)
                self._path_best = copy.deepcopy(partial)
            return

        for n in self._myGraph.neighbors(current_node):
            if n not in partial:
                if self._myGraph[current_node][n]["weight"] > soglia:
                    partial.append(n)
                    self._recursion(partial, soglia)
                    partial.pop()



    def _getEdgeWeight(self, u, v):
        return self._myGraph[u][v]["weight"]


    def _getWeight(self, listObj):
        totWeight = 0
        for n in range(len(listObj)-1):
            totWeight += self._myGraph[listObj[n]][listObj[n+1]]["weight"]
        return totWeight

    def _countValidNeighbors(self, n, soglia):
        counter = 0
        for v in self._myGraph.neighbors(n):
            if self._myGraph[n][v]["weight"] > soglia:
                counter += 1
        return counter


    def buildGraph(self):
        self._myGraph.clear()
        self._chrMap.clear()

        self._myGraph.add_nodes_from(self._getNodes())
        for n in self._myGraph.nodes:
            self._chrMap[n.number] = n
        self._addEdges()
        print(self._myGraph.nodes)
        i = 0
        for n in list(self._myGraph.nodes):
            i += 1
        print(i)
        print(len(self._myGraph.nodes))
        pass


    def _getNodes(self):
        return DAO.getAllChromosomes()


    def _addEdges(self):
        for e in list(DAO.getAllConnections(self._chrMap)):
            if e[0] != e[1] and not self._myGraph.has_edge(e[0], e[1]):
                self._myGraph.add_edge(e[0], e[1], weight=e[2])
        pass

    def getEdgesSoglia(self, soglia):
        maggiori = []
        minori = []
        for u,v, data in self._myGraph.edges(data=True):
            if data["weight"] > soglia:
                maggiori.append((u, v, data))
            elif data["weight"] < soglia:
                minori.append((u, v, data))
        return len(maggiori), len(minori)





