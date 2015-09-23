# -*- coding: utf-8 -*-
from collections import defaultdict
from collections import namedtuple
class Grafo(object):

    def __init__(self, conexoes, weighted=False): # Falta fazer o peso das arestas.
        self._ordem = 0
        self.grafo = defaultdict(dict)
        if weighted:
             self.peso = defaultdict(dict)
        self.adicionarVertice(conexoes, weighted)

    def adicionarVertice(self, conexoes, weighted=False):
        if weighted:
            if self._ordem != 0:
                for v1, v2, weight in conexoes:
                    self.adicionarAresta(v1, v2, weight, weighted)
            else:
                for v1 in conexoes:
                    self.grafo[v1]
        else:
            for v1, v2 in conexoes:
                self.adicionarAresta(v1, v2)

    def adicionarAresta(self, v1, v2, weight=0, weighted=False):
        if weighted:
            # Ligacao = namedtuple('Ligacao', ['weight','v2'])

            # l = Ligacao(weight, v2)
            # self.grafo[v1].add(l)
            # l = Ligacao(weight, v1)
            # self.grafo[v2].add(l)
            self.grafo[v1][v2] = weight
            self.grafo[v2][v1] = weight
            self._ordem += 1

        else:
            self.grafo[v1][v2]
            self.grafo[v2][v1]
            self._ordem += 1


    def removerVertice(self, v):
        #for vertice, ligacao in self.grafo.items():
        for vertice, adjacentes in self.grafo.items():
            try:
               adjacentes.pop(v, None)
            except KeyError:
                pass
        try:
            del self.grafo[v]
        except KeyError:
            pass
        self._ordem -= 1

    def removerAresta(self, v1, v2):
        try:
            del self.grafo[v1][v2]
        except KeyError:
            pass
        try:
            del self.grafo[v2][v1]
        except KeyError:
            pass

    def vertices():


    def conectado(self, v1, v2):

        if v2 in self.grafo[v1]:
            return True
        else:
            return False

    def ordem(self):
        return self._ordem


    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self.peso))