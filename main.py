from graph import Grafo

g = Grafo('A', True)
g.adicionarVertice('B')
g.adicionarVertice('C')
g.adicionarVertice('D')
g.adicionarVertice('E')
g.adicionarVertice('F')
g.adicionarVertice('G')
g.adicionarVertice('H')
g.adicionarVertice('I')
g.adicionarVertice('J')
g.adicionarVertice('K')
g.adicionarVertice('L')
g.adicionarVertice('M')
g.adicionarVertice('N')
g.adicionarVertice('P')



print(g.grafo)

g.adicionarAresta('A','B',9)
g.adicionarAresta('B', 'C', 10)
g.adicionarAresta('D', 'E', 8)
g.adicionarAresta('B', 'E', 2)
g.adicionarAresta('D', 'F', 1)
#g.adicionarAresta('F', 'A', 2)

g.adicionarAresta('G', 'H', 8)
g.adicionarAresta('H', 'I', 4)
g.adicionarAresta('H', 'J', 7)
g.adicionarAresta('G', 'M', 9)
g.adicionarAresta('M', 'N', 10)
g.adicionarAresta('N', 'P', 2)
#g.adicionarAresta('P', 'H', 7)
#g.adicionarAresta('A', 'W', 9)
print ("Peso da Aresta")
print g.peso('A', 'B')

print(g.grafo)

print g.ordem()

# g.removerVertice('A')
# print (g.grafo)
# print g.ordem()

print g.umVertice()

print g.vertices()

print ("Testa")
print g.adjacentes('B')

print g.grau('E')

print g.buscaCiclo('A')
