
"""
Karl Michel Koerich , 1631968
Thursday, March 29
R. Vincent , instructor
Assignment 3
"""

#Imports used
from BST import BST
from random import shuffle

#Creating BST to test methods
bst = BST()
bst.put('a', 0)
bst.put('d', 11)
bst.put('c', 0)
bst.put('b', 10)
bst.put('t', 14)
bst.put('y', 1)
bst.put('w', 76)
bst.put('u', 110)
#Test __repr__()
assert str(bst) == "{'a':0, 'b':10, 'c':0, 'd':11, 't':14, 'u':110, 'w':76, 'y':1}"
#Test get & contains
assert bst.get('t') == 14
assert bst.get('i') == None #Since they is no 'i'
assert bst.contains('t') == True
assert bst.contains('g') == False
#Test minKey & maxKey
assert bst.minKey() == 'a'
assert bst.maxKey() == 'y'
bst = BST()
assert bst.minKey() == None
assert bst.maxKey() == None

#End of tester code and start of performance code

print("{:>4}{:>4}{:>4}{:>8}".format("N", "MIN", "MAX", "MEAN"))

N_sizes = [32, 64, 128, 256]
N_of_BSTs = 100

for N in N_sizes:
	
	min = 0
	max = 0
	total = 0

	for times in range(0, N_of_BSTs):

		L = list(range(0, N))
		shuffle(L) #Shuffles list created above
		bst = BST() #Creates new BST
		
		for key in L: #Adds numbers to the BST
			bst.put(key)

		#Sets min e max value
		depth = bst.depth()
		if depth < min or min == 0:
			min = depth
		elif depth > max:
			max = depth
		total += depth

	mean = total/N_of_BSTs #Calculates mean value
	print("{:>4}{:>4}{:>4}{:>8}".format(N, min, max, mean))

	# By running the program a few times, 
	# I realized that the MIN and MAX values always increase by approx 2
	# 	when going from a lower N to a greater N. The consequence of that
	#	  is that the mean also increases by approx 2, as seen below:

	#	 N MIN MAX    MEAN
  	#	32   7  14    9.35	
  	#	64   9  16   11.72	- Min, Max and MEAN incresed by 2
 	#  128  11  19   14.19	- Min, Max and MEAN incresed by 2
 	#  256  14  22   16.52	- Min, Max and MEAN incresed by 2

	# I noticed that as you increase N exponentially (32, 64, 128, 256),
	# the mean depth increases approximately linearly (values around 9, 11, 14, 16).

	# Using this information, we are able to predict the aprox. depths for future
	# 	BSTs looking only at N.






