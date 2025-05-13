from database import DAO
import networkx as nx
class Model:
    def __init__(self):
        self._dao = DAO.DAO()
        self._graph = nx.Graph()
        self._idMap = {}

    def getColori(self):
        return self._dao.getColours()

    def createGraph(self, colore, anno):
        vertici = self._dao.getProdottiColore(colore)

        for vertice in vertici:
            self._idMap[vertice.Product_number] = vertice

        lista_vertici = self._idMap.keys()
        self._graph.add_nodes_from(lista_vertici)

        sales = self._dao.getSalesColore(lista_vertici)

        #sono gia filtrati per colore
        for (i1, s1) in enumerate(sales):
            abilita = False
            date_vendite = set()
            if s1.Date.year == anno:
                for i2 in range(i1+1, len(sales)):
                    if (sales[i2].Date.year == anno and s1.Product_number != sales[i2].Product_number and s1.Retailer_code == sales[i2].Retailer_code):
                        if (date_vendite.contains(sales[i2].date)):
                            abilita = True
                            v =  sales[i2].Product_number
                            date_vendite.add(s1.date)
                        else:
                            date_vendite.add(sales[i2].date)

                if abilita:
                    self._graph.add_edge(self._idMap[s1.Product_number], self._idMap[v], date_vendite.size())


