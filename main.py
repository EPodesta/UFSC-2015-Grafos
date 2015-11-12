from graph import Graph


print("Not Oriented:")

g1 = Graph('A', True)
g1.addVertex('B')
g1.addVertex('C')
g1.addVertex('D')
g1.addVertex('E')
g1.addVertex('F')
g1.addVertex('G')
g1.addVertex('H')
g1.addVertex('I')
g1.addVertex('J')
g1.addVertex('K')
g1.addVertex('L')
g1.addVertex('M')
g1.addVertex('N')
g1.addVertex('P')



print(g1.graph)

g1.addEdge('A','B',9)
g1.addEdge('B', 'C', 10)
g1.addEdge('D', 'E', 8)
g1.addEdge('B', 'E', 2)
g1.addEdge('D', 'F', 1)

g1.addEdge('H', 'G', 10)
g1.addEdge('P', 'G', 10)
g1.addEdge('W', 'G', 10)
g1.addEdge('G', 'H', 8)
g1.addEdge('H', 'I', 4)
g1.addEdge('H', 'J', 7)
g1.addEdge('G', 'M', 9)
g1.addEdge('M', 'N', 10)
g1.addEdge('N', 'P', 2)

print(g1.graph)

print ("Weight A -> B:")
print g1.weight('A', 'B')

print("Order")
print g1.order()

print("Degree of B:")
print g1.degree('B')

print("Get one vertex:")
print g1.oneVertex()

print("Get all vertices:")
print g1.vertices()

print("Get adjacents of B:")
print g1.adjacent('B')

print("searchCycle in this graph:")
print g1.searchCycle('A')

print("Predecessor of B")
print (g1.predecessor('B'))

print("Successor of B")
print(g1.successor('B'))

print("Oriented:")
g = Graph('A', True, True)
g.addVertex('B')
g.addVertex('C')
g.addVertex('D')
g.addVertex('E')
g.addVertex('F')



print(g.graph)

g.addEdge('A','B',9)
g.addEdge('B', 'C', 10)
g.addEdge('D', 'E', 8)
g.addEdge('B', 'E', 2)
g.addEdge('D', 'F', 1)


print(g.graph)

print ("Weight A -> B:")
print g.weight('A', 'B')

print("Order")
print g.order()

print("Degree of B:")
print g.degree('B')

print("Get one vertex:")
print g.oneVertex()

print("Get all vertices:")
print g.vertices()

print("Get adjacents of B:")
print g.adjacent('B')

print("Predecessor of G")
print (g.predecessor('G'))

print("Successor of G")
print(g.successor('G'))

print("Degree emission of B")
print(g.emissionDegree('B'))

print("Degree Reception of B")
print(g.receptionDegree('B'))
