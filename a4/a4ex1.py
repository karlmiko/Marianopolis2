"""
Karl Michel Koerich , 1631968
Friday , April 13
R. Vincent , instructor
Assignment 4
"""

#a4ex1.py

#
# It works with every single file in J5
#

from graph import *
from bfs import *

def constructGraph(path):
	'''Opens a file, reads it and constructs a graph
		according to its information.'''

	fp = open(path)
	v = int(fp.readline().strip())
	g = digraph(v) # Constructs the graph.

	for i in range(0, v): # Adds edges to vertex
	    values = []
	    for x in fp.readline().split()[1:]:
	        values.append(int(x))
	    for w in values:
	        g.addEdge(i, (w-1))

	return g

def isAllReachable(bfs, numberV):
	'''Checks to see if every page is reachable.'''

	for i in range(1, numberV):
	    if not bfs.hasPathTo(i):
	        return 'N'
	return 'Y'

def listFinalPages(g):
	'''Returns a list of all the final pages.'''

	allFinalPages = []
	for j in range(0, g.V()):
	    if g.adj(j) == []:
	        allFinalPages.append(j)

	return allFinalPages

def shortestPath(bfs, g):
	'''Finds shortest path to the end of the book.'''

	lenShort = 9999999999 # Arbitrary shortest path
	for finalPage in listFinalPages(g):
		if bfs.pathTo(finalPage) == None: # Ignore if there is no path to the page
			continue
		lenAdj = len(bfs.pathTo(finalPage))
		if lenAdj < lenShort: # Sets up new shortest path
			lenShort = lenAdj

	return lenShort

def pagesReach_shortPath(path):
	'''Identify if all pages are reachable and the shortest
		path to the end. Prints both results.'''

	g = constructGraph(path)
	numberV = g.V()
	bfs = BFS(g, 0)
	print()
	print(isAllReachable(bfs, numberV))
	print(shortestPath(bfs, g))

path = input("Enter a file name: ")
pagesReach_shortPath(path)





    








