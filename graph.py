# -*- coding: utf-8 -*-
from collections import defaultdict
import random



class Graph(object):
    """
    This class will represent a graph with its basic functions.
    """
    
    def __init__(self, initialVertex, weight=False, oriented=False):
        """
        Inicialize a graph. The init recieves the initial vertex and two boolean to set if the graph
        will be weighted or oriented.
        """
        self.graph = defaultdict(dict)
        self._oriented = oriented
        self._weight = weight
        self.addVertex(initialVertex)


    def addVertex(self, v1):
        """This method will add a vertex in the graph."""
        self.graph[v1]

    def addEdge(self, v1, v2, weight=0):
        """This method will connected two vertices and, if was especified, will add a weight."""

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
        """This method will remove a vertex in the graph."""
        for vertex, adjacent in self.graph.items():
            try:
               adjacent.pop(v, None)
            except KeyError:
                pass
        try:
            del self.graph[v]
        except KeyError:
            pass

    def deleteEdge(self, v1, v2):
        """This method will desconnect two vertices(delete an edge)."""
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

    def connected(self, v1, v2):
        """It will be verified if two vertices are connected."""
        return v2 in self.graph[v1]

    def order(self):
        """It will return the order of the graph."""
        return len(self.graph)

    def vertices(self):
        """It will be returned a set with all the vertices in the graph."""
        _set = set()
        for v, l in self.graph.items():
            _set.add(v)
        return _set

    def oneVertex(self):
        """This method will return a random vertex in the graph."""
        order = self.order()
        rand = random.randrange(1, order)
        count = 0
        for v, l in self.graph.items():
            if count == rand:
                return v
            count += 1

    def adjacent(self, v):
        """This method will return a set with all the adjacents of a vertex in a non-oriented graph."""
        _set = set()
        adj = self.graph[v]
        for vertex in adj:
            _set.add(vertex)
        return _set

    def successor(self, v):
        """It will return the successors of a vertex in an oriented graph."""
        if self._oriented:
            return self.graph[v]

    def predecessor(self, v):
        """It will return the predecessors of a vertex in an oriented graph."""
        if self._oriented:
            return {i for i in self.graph if v in self.graph[i]}

    def degree(self, v):
        """This method will return the quantity of edges of a vertex in a non-oriented graph."""
        adj = self.adjacent(v)
        return len(adj)

    def emissionDegree(self, v):
        """This method will return the emission degree of a vertex in an oriented graph."""
        return len(self.successor(v))

    def receptionDegree(self, v):
        """It will return the reception degree of a vertex in an oriented graph."""
        return len(self.predecessor(v))

    def weight(self, v1, v2):
        """It will return the weight of a connection between two vertices."""
        return self.graph[v1][v2]

    def depthFirstSearch(self, v, vA, alreadyVisited, l):
        """It will do a depth search in the graph, with the objective to find a cycle."""
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
        """
        This method is responsible to solve the problem with disconnected graphs that can
        occur if we utilize just the depthFirstSearch method.
        """
        l = self.vertices()
        _list = set()
        while True:
            try:
                x = l.pop()
            except KeyError:
                break
            if self.depthFirstSearch(x, None, _list,l):
                return True

        return False
        
    def __str__(self):
        """This method will be resposible for the print of the graph"""
        return '{}({})'.format(self.__class__.__name__, dict(self.weight))