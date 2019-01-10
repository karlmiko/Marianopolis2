class stack(list):
    '''A very simple stack class derived from a Python list.'''
    def isEmpty(self):
        '''return True if the stack is empty.'''
        return self == []

    def push(self, value):
        '''Add a value to the stack.'''
        self.append(value)

    def top(self):
        '''Check the top of the stack, without changing the stack.'''
        if self.isEmpty():
            raise ValueError("Stack underflow")
        return self[-1]

    def pop(self):
        '''Remove the top of the stack, returing the value found there.'''
        if self.isEmpty():
            raise ValueError("Stack underflow")
        return super().pop()
