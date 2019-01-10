
"""
Karl Michel Koerich , 1631968
Thursday, March 29
R. Vincent , instructor
Assignment 3
"""

class BST(object):
    '''Class that represents a Binary Search Tree.'''
    class Node(object):
        '''A single node within a BST.'''
        def __init__(self, key, val = None):
            self.key = key
            self.val = val
            self.left = None
            self.right = None

        def __repr__(self):
            if self.val == None:
                return repr(self.key)
            else:
                return repr(self.key) + ':' + repr(self.val)

    def __init__(self):
        self.root = None

    def __len__(self):
        '''Compute the size (number of key/value pairs) of the BST.'''
        def size(node):
            '''Compute the size of the tree below this node.'''
            if node == None:
                return 0
            else:
                return 1 + size(node.left) + size(node.right)
        return size(self.root)

    def __bool__(self):
        '''Convert a BST into a Boolean value. Like most Python collections,
        the logic here is that any non-empty BST evaluates as True.'''
        return self.root != None
    
    def put(self, key, val = None):
        '''Insert the key-value pair into
        the BST.'''
        def _put(node, key, val):
            if node == None:
                return BST.Node(key, val)
            elif key < node.key:
                node.left = _put(node.left, key, val)
            elif key > node.key:
                node.right = _put(node.right, key, val)
            else:
                node.val = val
            return node
        self.root = _put(self.root, key, val)

    @staticmethod
    def _get(node, key):
        '''Helper function for get() and contains()'''

        #Question 2.1
        while True:
            if node == None:
                return None
            elif key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                return node
            
    def get(self, key):
        '''Get the value associated with
        the given 'key'.'''
        x = self._get(self.root, key)
        if x == None:
            return None
        else:
            return x.val

    def contains(self, key):
        return self._get(self.root, key) != None

    def depth(self):
        '''Return the maximum depth of the tree.'''
        def depth(node):
            '''Compute the depth of the tree below this node.'''
            if node == None:
                return 0
            else:
                return 1 + max(depth(node.left), depth(node.right))
        return depth(self.root)

    #Question 2.2
    def minKey(self):
        '''Return the smallest (leftmost) key of the tree.'''
        
        node = self.root

        while True:
        	if node == None:
        		return #If the BST is empty, returns None
        	elif node.left == None:
        		return node.key
        	node = node.left

    #Question 2.2
    def maxKey(self):
        '''Return the largest (rightmost) key of the tree.'''

        node = self.root

        while True:
        	if node == None:
        		return #If the BST is empty, returns None
        	elif node.right == None:
        		return node.key
        	node = node.right

    #Question 2.3
    def traverse(self, func):
        ''' Perform inorder , left -to - right
                traversal of BST rooted at node 'x '. '''
        def inorder (x, func):
            if x == None :
                return
            inorder (x.left , func) #traverse left
            func (x) #visit node
            inorder (x.right , func) #traverse right
        
        x = self.root
        inorder(x, func)

    #Question 2.4
    def __repr__(self):
    	'''Converts the entire tree into a useful string.'''

    	string_repr = "{"

    	def helper(x):
    		#nonlocal used to modify the nearest string_repr outside
    		nonlocal string_repr
    		string_repr += (x.__repr__() + ", ")

    	self.traverse(helper)
    	string_repr = string_repr[:-2] + "}" #Removes last 2 character and closes with }
    	return string_repr






    
        

        
                

