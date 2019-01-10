# Linked list class and support classes.
#
class ListNode(object):
    '''Represents an item on a linked list.

    There are two attributes, one to hold the value stored in
    the list, the next "points" to the next node on the list.
    The last node on the list always has its link set to some
    "sentinel" value, such as None in Python or null in Java.
    '''
    def __init__(self, value = None):
        '''Construct a list node.'''
        self.value = value
        self.link = None

class SinglyLinkedList(object):
    '''Class that defines a relatively simple linked list, with a
    single link leading from a predecessor node to a successor node.

    Implements several methods, modeled on those in the standard
    list() class. In addition, implements a "prepend()" method that
    illustrates adding an element to the beginning of a list.

    Methods of the standard list class that we do not implement include:
    clear(), copy(), extend(), __add__(), __mul__(), reverse(), and sort().
    '''
    def __init__(self, iterable = None):
        '''Creates a new list, initialized to the contents of 
        'iterable'.'''
        self.head = None
        if iterable != None:
            previous = None
            for value in iterable:
                newnode = ListNode(value)
                if previous == None:
                    self.head = newnode
                else:
                    previous.link = newnode
                previous = newnode

    def prepend(self, value):
        '''Add an element to the beginning of the list.

        This is the easiest case. All we need to do is:
        1) create the new list node
        2) set the link field of the new node to the
        current list head.
        3) set the current list head to this node.
        '''
        node = ListNode(value)
        node.link = self.head
        self.head = node

    def get(self, index):
        '''Get the value stored at a particular index
        of the linked list.

        To accomplish this, we have to look through every node
        on the list, counting up as we go. When the count reaches
        the index, we return the value found there.'''
        count = 0
        node = self.head
        while node != None:
            if count == index:
                return node.value
            node = node.link
            count += 1
        raise IndexError('list index out of range')

    def count(self, value):
        '''Count the number of list nodes with values equal to the
        'value'.'''
        count = 0
        node = self.head
        while node != None:
            if node.value == value:
                count += 1
            node = node.link
        return count

    def index(self, value):
        '''Return the index of the first list element that matches
        the given 'value'.'''
        count = 0
        node = self.head
        while node != None:
            if node.value == value:
                return count
            count += 1
            node = node.link
        raise ValueError('Value ' + str(value) + ' not found.')
            
    def append(self, value):
        '''Add an element to the end of the linked list.

        This method has to be a bit more complex than the
        prepend() method, in that we have to search to the
        end of the list, and insert the new node there.
        '''
        node = self.head
        if node == None:    # Empty list
            self.head = ListNode(value)
        else:
            while node.link != None:
                node = node.link
            node.link = ListNode(value)

    def insert(self, index, value):
        '''Add an element at a particular index of a linked
        list.
        If the index is greater than the length of the list, the
        new node is just appended to the list.'''
        newnode = ListNode(value)
        node = self.head
        if index == 0:
            newnode.link = self.head
            self.head = newnode
        else:
            count = 1
            while node.link != None and count < index:
                node = node.link
                count += 1
            newnode.link = node.link
            node.link = newnode
        
    def remove(self, value):
        '''Remove the first element that matches 'value' from the list.'''
        previous = None
        node = self.head
        while node != None and node.value != value:
            previous = node
            node = node.link
        if node == None:
            raise ValueError('Value ' + str(value) + ' not found.')
        elif previous != None:
            previous.link = node.link
        else:
            self.head = node.link

    def pop(self, index = -1):
        '''Removes an node from the list based on a given
        index. If the index is -1, the last node on list is
        removed. Returns the value associated with the deleted
        node.'''
        count = 0
        previous = None
        node = self.head
        if index >= 0:
            while node != None and count != index:
                count += 1
                previous = node
                node = node.link
        else:
            while node != None and node.link != None:
                previous = node
                node = node.link
        if node == None:
            raise ValueError('Position ' + str(index) + ' not found.')
        
        if previous != None:
            previous.link = node.link
        else:
            self.head = node.link

        return node.value

    def __bool__(self):
        '''Returns True if the list is non-empty.

        This method is called implicitly when a value of our class
        is converted to a boolean value.'''
        return self.head != None

    def __len__(self):
        '''Returns the total number of nodes on the list.

        This method is called implicitly when the len() function
        is used with values of this class.'''
        count = 0
        node = self.head
        while node != None:
            count += 1       # count the node
            node = node.link # go to the next node
        return count

    def __str__(self):
        '''Convert a linked list to a string representation.

        This method is called implicitly when the str() function
        is used with values of this class.
        '''
        node = self.head
        r = '['
        while node != None:
            r += str(node.value)
            if node.link != None: # If not at the end,
                r += ', '         #  add a comma and space.
            node = node.link
        r += ']'
        return r

    def __eq__(self, other):
        '''Compare two linked lists for equality.

        This method is called when a SinglyLinkedList is
        compared with '==' or '!='.
        '''
        node1 = self.head
        node2 = other.head
        while node1 != None and node2 != None:
            if node1.value != node2.value:
                return False
            node1 = node1.link
            node2 = node2.link
        return node1 == None and node2 == None

### Testing code ###
#
# As of now, the testing code is quite haphazard, but it attempts
# to exercise all of the features of the class, as well as running a
# simple performance check to illustrate some of the performance differences
# compared with the Python list() class.
#
if __name__ == "__main__":
    print("Testing the SinglyLinkedList class.")
    r = SinglyLinkedList()
    for x in range(1, 10, 2):
        r.prepend(x)
    for v in r:
        print(v)
