from graph import Graph


print("Not Oriented:")

g = Graph('A', True)
g.addVertex('B')
g.addVertex('C')
g.addVertex('D')
g.addVertex('E')
g.addVertex('F')
g.addVertex('G')
g.addVertex('H')
g.addVertex('I')
g.addVertex('J')
g.addVertex('K')
g.addVertex('L')
g.addVertex('M')
g.addVertex('N')
g.addVertex('P')



print(g.graph)

g.addEdge('A','B',9)
g.addEdge('B', 'C', 10)
g.addEdge('D', 'E', 8)
g.addEdge('B', 'E', 2)
g.addEdge('D', 'F', 1)
#g.addEdge('F', 'A', 2)

g.addEdge('H', 'G', 10)
g.addEdge('P', 'G', 10)
g.addEdge('W', 'G', 10)
g.addEdge('G', 'H', 8)
g.addEdge('H', 'I', 4)
g.addEdge('H', 'J', 7)
g.addEdge('G', 'M', 9)
g.addEdge('M', 'N', 10)
g.addEdge('N', 'P', 2)
#g.addEdge('P', 'H', 7)
#g.addEdge('A', 'W', 9)
print(g.graph)

print ("Weight A -> B:")
print g.weight('A', 'B')

print("Order")
print g.order()

# g.removerVertice('A')
# print (g.grafo)
# print g.ordem()
print("Get one vertex:")
print g.oneVertex()

print("Get all vertexes:")
print g.vertexes()

print("Get adjacents of B:")
print g.adjacent('B')

# print g.grau('E')
print("searchCycle in this graph:")
print g.searchCycle('A')

print("Predecessor of G")
print (g.predecessor('G'))

print("Successor of G")
print(g.successor('G'))

print("Oriented:")
g = Graph('A', True, True)
g.addVertex('B')
g.addVertex('C')
g.addVertex('D')
g.addVertex('E')
g.addVertex('F')
g.addVertex('G')
g.addVertex('H')
g.addVertex('I')
g.addVertex('J')
g.addVertex('K')
g.addVertex('L')
g.addVertex('M')
g.addVertex('N')
g.addVertex('P')



print(g.graph)

g.addEdge('A','B',9)
g.addEdge('B', 'C', 10)
g.addEdge('D', 'E', 8)
g.addEdge('B', 'E', 2)
g.addEdge('D', 'F', 1)
#g.addEdge('F', 'A', 2)

g.addEdge('H', 'G', 10)
g.addEdge('P', 'G', 10)
g.addEdge('W', 'G', 10)
g.addEdge('G', 'H', 8)
g.addEdge('H', 'I', 4)
g.addEdge('H', 'J', 7)
g.addEdge('G', 'M', 9)
g.addEdge('M', 'N', 10)
g.addEdge('N', 'P', 2)
#g.addEdge('P', 'H', 7)
#g.addEdge('A', 'W', 9)
print(g.graph)

print ("Weight A -> B:")
print g.weight('A', 'B')

print("Order")
print g.order()

# g.removerVertice('A')
# print (g.grafo)
# print g.ordem()
print("Get one vertex:")
print g.oneVertex()

print("Get all vertexes:")
print g.vertexes()

print("Get adjacents of B:")
print g.adjacent('B')

# print g.grau('E')
print("searchCycle in this graph:")
print g.searchCycle('A')

print("Predecessor of G")
print (g.predecessor('G'))

print("Successor of G")
print(g.successor('G'))
