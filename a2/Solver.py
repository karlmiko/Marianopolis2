"""
Karl Michel Koerich , 1631968
Friday, March 16
R. Vincent , instructor
Assignment 2
"""

# Main program for assignment 2. Your job here is to finish the
# __init__ method to solve the puzzle as described in the handout.
#

from MinPQ import MinPQ
from Board import Board

import functools
@functools.total_ordering
class Node(object):
    def __init__(self, bd, moves, node):
        '''Construct a new node object.'''
        self.board = bd         # save the board
        self.moves = moves      # number of moves to reach this board.
        self.cost = bd.distance() # save the distance metric.
        self.previous = node      # save the previous node.
    def __gt__(self, other):
        '''A node is 'greater' than another if the cost plus the
        number of moves is larger.'''
        return (self.cost + self.moves) > (other.cost + other.moves)
    def __eq__(self, other):
        '''Test two nodes for equality.'''
        if self is other:
            return True
        if other is None or type(other) != Node:
            return False
        return (self.cost + self.moves) == (other.cost + other.moves)
  
class Solver(object):
    def __init__(self, initial):
        # This is where your code to solve the puzzle will go! You may
        # change or replace the following two lines:

        self.__solvable = False
        self.__trace = []

        minPq = MinPQ() #Creates the MinPQ
        currentNode = Node(initial, 0, None) #First node containing the initial board
        minPq.insert(currentNode) #Adds the first node

        self.__size = 1 #Keeps track of the size of MinPQ

        while not minPq.isEmpty():
            
            #Removes the best node from the MinPQ
            currentNode = minPq.delMin()
            self.__size -= 1
            
            #In case this node contains the final board, it traces the path and leave the loop
            if currentNode.board.solved():
                while currentNode != None:
                    self.__trace += [currentNode.board]
                    currentNode = currentNode.previous
                    self.__solvable = True
                break

            neighbors = currentNode.board.neighbors() #Gets the list of neighbors for the current position
            
            for boardN in neighbors:
                #Only considers new positions as potential moves
                if currentNode.previous == None or boardN != currentNode.previous.board:
                    #Creates new node with moved board and add it to minPQ
                    newNode = Node(boardN, currentNode.moves+1, currentNode)
                    minPq.insert(newNode)
                    self.__size += 1

    def solvable(self):
        '''Returns True if this puzzle can be solved.'''
        return self.__solvable;
  
    def moves(self):
        '''Returns the number of moves in the solution, or -1 if
        not solvable.'''
        return len(self.__trace) - 1 if self.__solvable else -1
  
    def solution(self):
        '''Returns the list of board positions in the solution.'''
        return self.__trace.copy()

    def size(self):
        '''Returns the maximum size of the primary queue'''
        return self.__size

# Add your main program here. It should prompt for a file name, read
# the file, and create and run the Solver class to find the solution
# for the puzzle. Then it should print the result (see the example output
# file for details).
#

puzzles = ["puzzle4x4-01.txt", "puzzle4x4-02.txt", 
"puzzle4x4-03.txt", "puzzle4x4-04.txt", "puzzle4x4-06.txt", 
"puzzle4x4-09.txt", "puzzle4x4-10.txt", "puzzle4x4-12.txt", "puzzle4x4-14.txt", 
"puzzle4x4-16.txt", "puzzle4x4-18.txt", "puzzle4x4-20.txt", "puzzle4x4-unsolvable.txt"]

print ("These are a few of the existing puzzles...\n")

#Prints the existing puzzles to make it easier for the user
for p in puzzles:
    print (p)

#Opens the file, read it and trsnaform it into a new board
fileName = "puzzles/" + input("\nType the name of the puzzle you wish to solve and press enter: ")
file = open(fileName)
myLines = file.read()
newBoard = Board(myLines)

solver = Solver(newBoard) #Creates solver to find the solution for the puzzle

#Prints the steps of the solution
move = 0
listOfMoves = solver.solution()[::-1]
print ("\nMinimum number of moves = " + str(len(listOfMoves)-1))

#The following line was used for Ex.2
#print ("Maximum size of the priority queue = " + str(solver.size()))

for board in listOfMoves:
    print ("Move # " + str(move))
    print (board)
    move += 1
    
file.close() #Close the file











