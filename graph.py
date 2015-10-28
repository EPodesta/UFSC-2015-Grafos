# -*- coding: utf-8 -*-
from collections import defaultdict
import random
#Essa classe será responsável por representar um grafo, possuindo as funções
#básicas para sua representação.
class Graph(object):

#Inicializa o grafo. O init recebe como parâmetro o vértice inicial, um boolean
#para determinar se possui peso ou não e outro boolean para determinar se o grafo
#será orientado ou não. A base para esse grafo foi um Dicionário de Dicionários.
    def __init__(self, initialVertex, weight=False, oriented=False):
        self.graph = defaultdict(dict)
        self._oriented = oriented
        self._weight = weight
        self.addVertex(initialVertex)

#Esse método adicionará um vértice no grafo(dicionário).
    def addVertex(self, v1):
        self.graph[v1]

#O método addEdge irá conectar dois vértices e, caso tenha sido especificado que o grafo
#será valorado, atribuir um peso.
    def addEdge(self, v1, v2, weight=0):

        if not self._oriented:
            if self._weight:
                self.graph[v1][v2] = weight
                self.graph[v2][v1] = weight
    
            else:
    
                self.graph[v1][v2]
                self.graph[v2][v1]
        else:
            if self._weight:
                self.graph[v1][v2] = weight

            else:
                self.graph[v1][v2]

    def deleteVertex(self, v):
        for vertex, adjacent in self.graph.items():
            try:
               adjacent.pop(v, None)
            except KeyError:
                pass
        try:
            del self.graph[v]
        except KeyError:
            pass

#O método deleteEdge desconectará dois vértices.
    def deleteEdge(self, v1, v2):
        if not self._oriented:
            try:
                del self.graph[v1][v2]
            except KeyError:
                pass
            try:
                del self.graph[v2][v1]
            except KeyError:
                pass
        else:
            try:
                del self.graph[v1][v2]
            except KeyError:
                pass 
#O método connected verificará se dois vértices estão conectados em um grafo.
    def connected(self, v1, v2):

        if v2 in self.graph[v1]:
            return True
        else:
            return False

#O método order retornará a ordem do Grafo(Número de vértices).
    def order(self):
        return len(self.graph)

#O método vertexes irá retornar um set com todos os vértices do Grafo.
    def vertexes(self):
        _set = set()
        for v, l in self.graph.items():
            _set.add(v)
        return _set

#OneVertex coletará um vértice aleatório do grafo.
    def oneVertex(self):
        order = self.order()
        rand = random.randrange(1, order)
        count = 0
        for v, l in self.graph.items():
            if count == rand:
                return v
            count += 1

#O método adjacent retornará um set com todos os vértices adjacentes a outro vértice.
    def adjacent(self, v):
        adj = self.graph[v]
        _set = set()
        for vertex in adj:
            _set.add(vertex)
        return _set

#O método successor será responsável por coletar os sucessores de um vértice em um grafo
#orientado.
    def successor(self, v):
        if self._oriented:
            return self.graph[v]
        else:
            print("Successor only makes sense in a oriented graph!")

#O método predecessor retornará os predecessores de um dado vértice em um grafo orientado.
    def predecessor(self, v):
        if self._oriented:
            return {i for i in self.graph if v in self.graph[i]}
        else:
            print("Predecessor only makes sense in a oriented graph!")

#O método degree retornará a quantidade de arestas de um dado vértice, ou seja, seu grau.
    def degree(self, v):
        adj = self.adjacent(v)
        count = 0
        for vertexes in adj:
            count += 1
        return count

#O método weight retornará o peso de uma aresta, sendo especificada pelos vértices que ela conecta.
    def weight(self, v1, v2):
        return self.graph[v1][v2]

#Os métodos depthFirstSearch e searchCycle farão uma busca por profundidade no grafo,
#seguindo como objetivo verificar se há ciclos no grafo.
    def depthFirstSearch(self, v, vA, alreadyVisited, l):
        if v in alreadyVisited:
            return True
        alreadyVisited.add(v)
        if vA != None:
            l.remove(v)
        for x in self.adjacent(v):
            if x != vA:
                if self.depthFirstSearch(x, v, alreadyVisited, l):
                    return True
        return False

    def searchCycle(self, v):
        l = self.vertexes()
        _list = set()
        while True:
            try:
                x = l.pop()
            except KeyError:
                break
            if self.depthFirstSearch(x, None, _list,l):
                return True

        return False
        
#Método determinado para "printar" o grafo.
    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self.weight))