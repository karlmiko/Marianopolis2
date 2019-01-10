from collections import deque
class BFS(object):
    '''Basic implementation of breadth-first search for Assignment 4.'''
    def __init__(self, G, s):
        '''Initialize the object and perform BFS from vertex 's'.'''
        self.__s = s            # start vertex.
        self.__distTo = [-1] * G.V() # distance to vertex.
        self.__edgeTo = [-1] * G.V() # edgeTo defines the SPT.

        vertices = deque([s])
        self.__distTo[s] = 0
        while vertices:
            v = vertices.popleft() # get next vertex.
            d = self.__distTo[v] + 1
            for w in G.adj(v):
                if self.__distTo[w] < 0: # not visited?
                    vertices.append(w)
                    self.__distTo[w] = d
                    self.__edgeTo[w] = v

    def hasPathTo(self, v):
        '''Returns True if there is a path from 's' to 'v'.'''
        return self.__distTo[v] >= 0

    def pathTo(self, v):
        '''Returns the shortest path from 's' to 'v' as a list of
        integer vertices.'''
        if not self.hasPathTo(v):
            return None         # If no path, return None
        path = []
        x = v                   # Build the path based on the edgeTo values.
        while x != self.__s:
            path = [x] + path
            x = self.__edgeTo[x]
        return [self.__s] + path

    def distTo(self, v):
        '''Returns the distance (number of edges) from 's' to 'v'.'''
        return self.__distTo[v]

    def V(self):
        '''Returns the number of vertices in the graph.'''
        return len(self.__distTo)

if __name__ == "__main__":
    from graph import graph
    G = graph.fromfile(open('tinyG.txt'))
    bfs = BFS(G, 0)
    assert bfs.hasPathTo(1) and bfs.distTo(1) == 1 and bfs.pathTo(1) == [0, 1]
    assert bfs.hasPathTo(2) and bfs.distTo(2) == 1 and bfs.pathTo(2) == [0, 2]
    assert bfs.hasPathTo(3) and bfs.distTo(3) == 2 and bfs.pathTo(3) == [0, 5, 3]
    for v in range(7, G.V()):
        assert not bfs.hasPathTo(v)
    print("All tests passed.")
