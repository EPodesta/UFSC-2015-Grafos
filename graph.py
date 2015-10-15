# -*- coding: utf-8 -*-
from collections import defaultdict
import random
class Grafo(object):

    def __init__(self, verticeInicial, weight=False, orientado=False):
        self._ordem = 0
        self.grafo = defaultdict(dict)
        self._orientado = orientado
        self._weight = weight
        self.adicionarVertice(verticeInicial)

    def adicionarVertice(self, v1):
        self.grafo[v1]
        self._ordem += 1

#conecta
    def adicionarAresta(self, v1, v2, weight=0):

        if not self._orientado:
            if self._weight:
                self.grafo[v1][v2] = weight
                self.grafo[v2][v1] = weight
    
            else:
    
                self.grafo[v1][v2]
                self.grafo[v2][v1]
        else:
            if self._weight:
                self.grafo[v1][v2] = weight

            else:
                self.grafo[v1][v2]

    def removerVertice(self, v):
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

#desconecta
    def removerAresta(self, v1, v2):
        if not self._orientado:
            try:
                del self.grafo[v1][v2]
            except KeyError:
                pass
            try:
                del self.grafo[v2][v1]
            except KeyError:
                pass
        else:
            try:
                del self.grafo[v1][v2]
            except KeyError:
                pass 

    def conectado(self, v1, v2):

        if v2 in self.grafo[v1]:
            return True
        else:
            return False

    def ordem(self):
        return self._ordem

    def vertices(self):
        conjunto = set()
        for v, l in self.grafo.items():
            conjunto.add(v)
        return conjunto

    def umVertice(self):
        rand = random.randrange(1, self._ordem)
        count = 0
        for v, l in self.grafo.items():
            if count == rand:
                return v
            count += 1

    def adjacentes(self, v):
        adj = self.grafo[v]
        conjunto = set()
        for vertices in adj:
            conjunto.add(vertices)
        return conjunto

    def grauSucessores(self, v):
        return self.grafo[v]

    def grauAntecessores(self, v):
        return {i for i in self.grafo if v in self.grafo[i]}


    def grau(self, v):
        adj = self.adjacentes(v)
        count = 0
        for vertices in adj:
            count += 1
        return count

    def peso(self, v1, v2):
        return self.grafo[v1][v2]

    def buscaProfundidade(self, v, vA, jaVisitados, l):
        if v in jaVisitados:
            return True
        jaVisitados.add(v)
        if vA != None:
            l.remove(v)
        for x in self.adjacentes(v):
            if x != vA:
                if self.buscaProfundidade(x, v, jaVisitados, l):
                    return True
        return False
# def buscaLargura():


    def buscaCiclo(self, v):
        l = self.vertices()
        lista = set()
        while True:
            try:
                x = l.pop()
            except KeyError:
                break
            if self.buscaProfundidade(x, None, lista,l):
                return True

        return False

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self.peso))