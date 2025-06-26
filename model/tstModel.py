import model as m

mymodel = m.Model()

grafo = mymodel.createGraph("White", 2018)

print(grafo)

print(mymodel.trovaPercorso(94110))
