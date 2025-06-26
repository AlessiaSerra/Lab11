import copy

from database import DAO
import networkx as nx
from arco import Arco

class Model:
    def __init__(self):
        self._dao = DAO.DAO()
        self._graph = nx.Graph()
        self._idMap = {}

    def getColori(self):
        return self._dao.getColours()

    def createGraph(self, colore, anno):
        self._graph.clear()
        nodes = self._dao.getProdottiColore(colore)
        self._graph.add_nodes_from(nodes)

        for node in nodes:
            self._idMap[node.Product_number] = node

        for p1 in nodes:
            for p2 in nodes:
                if p1 != p2:
                    count = self._dao.getSales(p1.Product_number, p2.Product_number, anno)
                    if count>0:
                        self._graph.add_edge(p1, p2, weight=count)


        return self._graph.number_of_nodes(), self._graph.number_of_edges()

    def getTop3(self):
        archi = self._graph.edges()

        pesi = self._graph.edges(data=True)

        archi = sorted(pesi, key=lambda e: e[2]['weight'], reverse=True)
        print(archi[:3])
        return archi[:3]

    def getNodiRipetuti(self, archi):
        collegati = []
        ripetuti = []
        for arco in archi:
            if arco[0].Product_number in collegati:
                ripetuti.append(arco[0].Product_number)
            if arco[1].Product_number in collegati:
                ripetuti.append(arco[1].Product_number)

            collegati.append(arco[0].Product_number)
            collegati.append(arco[1].Product_number)
        return ripetuti

    def trovaPercorso(self, partenza):
        parziale = [self._idMap[partenza]]
        self.sol_best = []
        self.best_value = 0

        viciniAmmissibili = self.viciniAmmissibili(parziale)
        for el in viciniAmmissibili:
            parziale.append(el)
            self._ricorsione(parziale)
            parziale.pop()

        return len(self.sol_best)-1


    def _ricorsione(self,parziale):
        viciniAmmissibili = self.viciniAmmissibili(parziale)
        if (len(viciniAmmissibili) == 0):
            if len(parziale) > len(self.sol_best):
                self.sol_best = copy.deepcopy(parziale)
                return

        for el in viciniAmmissibili:
            parziale.append(el)
            self._ricorsione(parziale)
            parziale.pop()



    def viciniAmmissibili(self, seq):
        vicini = self._graph.neighbors(seq[-1])
        res = []

        for vicino in vicini:
            if(len(seq)>=2):
                if (vicino not in seq and
                        self._graph[seq[-1]][vicino]['weight'] >= self._graph[seq[-2]][seq[-1]]['weight']):
                    res.append(vicino)
            else:
                if vicino not in seq:
                    res.append(vicino)

        return res


