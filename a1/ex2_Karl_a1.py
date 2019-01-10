"""
Karl Michel Koerich , 1631968
Friday , February 22, 2018
R. Vincent , instructor
Assignment 1
"""

#ex2_Karl_a1.py

from stack import stack

def findLeftIndex(char, rigths):

	c = 0
	for r in rights:
		
		if r == char:
			return c
		c += 1
 
lefts = ["(", "[", "{"]
rights = [")", "]", "}"]
files = ["test1.py", "test2.py", "test3.py", "test4.py", "test5.py"]

for fileName in files:

	syntaxStack = stack()
	file = open(fileName)

	for line in file:
		
		for char in line:

			if char in lefts:
				syntaxStack.push(char)

			elif char in rights:
				
				if not syntaxStack.isEmpty() and syntaxStack.top() == lefts[findLeftIndex(char, rights)]:
					syntaxStack.pop()
				else:
					syntaxStack.push(char)

	file.close()
	print(fileName, " valid syntax:  ", syntaxStack.isEmpty(), " -> ", syntaxStack)
