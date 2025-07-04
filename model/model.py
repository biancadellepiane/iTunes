import networkx as nx
from click import clear

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._idMap = {}
        self._idMapTitle = {}

    def buildGraph(self, d):
        self._graph.clear()
        nodes = DAO.getAllNodes(d)
        for n in nodes:
            self._idMap[n.AlbumId] = n

        for no in nodes:
            self._idMapTitle[no.Title] = no

        self._graph.add_nodes_from(nodes)

        archi = DAO.getAllEdges(self._idMap)
        self._graph.add_edges_from(archi)

    def graphDetails(self):
        return self._graph.number_of_nodes(), self._graph.number_of_edges()

    def getAllAlbum(self):
        return list(self._graph.nodes())

    def getComponenteConnessa(self, a):
        album = self._idMapTitle[a]
        cc = nx.node_connected_component(self._graph, album)
        return len(cc), self.getDurataTot(cc)

    def getDurataTot(self, cc):
        sum = 0
        for a in cc:
            sum += a.dTot #chimato in album.py
        return sum





