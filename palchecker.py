class Node(object):
    """
    A class to represent a node.

    ...

    Attributes
    ----------
    data : int or float
        An individual character or number to be stored in a node
    next_node : object of class Node
        A pointer to the next node in a stack or queue

    Methods
    -------
    setData(data):
        Updates the value of data attribute of Node
    setNext(next_node):
        Updates the value of next_node attribute of Node
    getData():
        Returns the value of data attribute
    getNext():
        Returns the value of next_node attribute
    """
    def __init__(self, data = None, next_node = None):
        """
        Constructs (or initializes) the attributes for an object of the class

        ...

        Parameters
        ----------
        data : int or float
            An individual character or number to be stored in a node
        next_node : object of class Node
            A pointer to the next node in a stack or queue

        """
        self.__data = data
        self.__next_node = next_node

    def setData(self, data):
        '''Set the "data" data field to the corresponding input.'''
        self.__data = data

    def setNext(self, next_node):
        '''Set the "next_node" data field to the corresponding input.'''
        self.__next_node = next_node

    def getData(self):
        '''Return the "data" data field.'''
        return self.__data

    def getNext(self):
        '''Return the "next_node" data field.'''
        return self.__next_node

class Queue(object):
    """
    A class to represent a queue.

    ...

    Attributes
    ----------
    head : object of class Node
        A pointer to the first Node of the queue
    tail : object of class Node
        A pointer to the last Node of the queue

    Methods
    -------
    enqueue(newData):
        Adds a new node with newData to the queue
    dequeue():
        Returns value of node at head, and removes it from queue
    isEmpty():
        Returns True or False based on if queue is empty
    """
    def __init__(self):
        '''Initialize queue to be empty'''
        self.__head = None
        self.__tail = None

    def __str__(self):
        '''Loop through your queue and print each Node's data.'''
        # Set current node to head
        current_node = self.__head

        if self.isEmpty():
            return "The queue is empty"

        final_string = "["

        # While the current Node is not None, compile strings,
        # then set current node to next code
        while current_node.getNext() is not None:
            final_string += str(current_node.getData()) + ", "
            current_node = current_node.getNext()

        # Now extract data from tail
        final_string += str(self.__tail.getData()) + "]"
        return final_string

    def enqueue(self, newData):
        '''Create a new node whose data is newData and whose next node is null
        Update head and tail.'''
        # Creat a new node with the data
        newNode = Node(newData)

        # If the queue is empty, make the newNode the head,
        # else, add it after the tail
        if self.isEmpty():
            self.__head = newNode
        else:
            self.__tail.setNext(newNode)

        # Set newNode to be the new tail
        self.__tail = newNode

    def dequeue(self):
        '''Return the head of the Queue
        Update head.'''
        # If empty, raise error, else save data and change head,
        # then return data
        try:
            if self.isEmpty():
                raise AttributeError
            else:
                data = self.__head.getData()
                next_node = self.__head.getNext()
                self.__head = next_node
                return data

        except AttributeError:
            print("The Queue is empty")
            raise AttributeError

    def isEmpty(self):
        '''Check if the Queue is empty.'''
        # Check if self.__head is none,
        # if it is, the queue is empty
        if self.__head is None:
            return True
        return False


class Stack(object):
    """
    A class to represent a stack.

    ...

    Attributes
    ----------
    top : object of class Node
        A pointer to the top of the stack

    Methods
    -------
    push(newData):
        Adds a new node with newData to the top of the stack
    pop():
        Returns value of node at the top, and removes it from the stack
    isEmpty():
        Returns True or False based on if stack is empty
    """
    def __init__(self):
        ''' We want to initialize our Stack to be empty.
        (ie) Set top as null'''
        self.__top = None

    def __str__(self):
        '''Loop through your stack and print each Node's data.'''
        # Set current node to top
        current_node = self.__top

        if self.isEmpty():
            return "The stack is empty"

        final_string = "["

        # While the current Node is not None, compile strings,
        # then set current node to next code
        while current_node.getNext() is not None:
            final_string += str(current_node.getData()) + ", "
            current_node = current_node.getNext()

        # Now extract data from final element
        final_string += str(current_node.getData()) + "]"
        return final_string

    def push(self, newData):
        '''We want to create a node whose data is newData and next node is top.
        Push this new node onto the stack
        Update top'''
        # Setting newNode with next node being current top
        newNode = Node(newData, self.__top)

        # setting newNode as new top
        self.__top = newNode

    def pop(self):
        ''' Return the Node that currently represents the top of the stack.
        Update top'''
        # If empty, raise error, else save data and change top,
        # then return data
        try:
            if self.isEmpty():
                raise AttributeError
            else:
                data = self.__top.getData()
                next_node = self.__top.getNext()
                self.__top = next_node
                return data

        except AttributeError:
            print("The Stack is empty")
            raise AttributeError

    def isEmpty(self):
        '''Check if the Stack is empty.'''
        # If there is nothing stored in top, it is empty
        if self.__top is None:
            return True
        return False

class TwoStackQueue(object):
    """
    A class to represent a two stack queue.

    ...

    Attributes
    ----------
    head : object of class Stack
        A pointer to the first Stack of the queue
    tail : object of class Stack
        A pointer to the second Stack of the queue

    Methods
    -------
    enqueue(newData):
        Adds a new node with newData to the bottom of head stack
    dequeue():
        Returns value of node at top of head stack, and removes it from queue
    isEmpty():
        Returns True or False based on if head stack is empty
    """
    def __init__(self):
        '''Initialize queue to be empty stacks'''
        self.__head = Stack()
        self.__tail = Stack()

    def __str__(self):
        '''represent two stack queue in string form'''

        if self.isEmpty():
            return "The Two Stack Queue is empty"

        final_string = "["

        # When the head stack is not empty, pop it to tail stack while
        # saving the value to the string, after it's all done,
        # move everything back to head stack
        while not self.__head.isEmpty():
            value = self.__head.pop().getData()
            print(value)
            final_string += str(value)
            self.__tail.push(value)
            # check if it's the last value to know if need to add ', '
            if not self.__head.isEmpty():
                final_string += ", "
        while not self.__tail.isEmpty():
            self.__head.push(self.__tail.pop())

        return final_string + "]"

    def enqueue(self, newData):
        '''Create a new node whose data is newData
        and add to head stack'''
        # Creat a new node with the data
        newNode = Node(newData)

        # If the queue is empty, push newNode onto head stack
        if self.isEmpty():
            self.__head.push(newNode)
        else:
            # push all nodes from head stack to tail stack,
            # add newNode onto head stack, then push everything
            # from tail stack back, so that head stack is in
            # first in, first out order
            while not self.__head.isEmpty():
                self.__tail.push(self.__head.pop())
            self.__head.push(newNode)
            while not self.__tail.isEmpty():
                self.__head.push(self.__tail.pop())

    def dequeue(self):
        '''Return the top of the head stack and pop it off'''
        # Use pop function and get data
        return self.__head.pop().getData()

    def isEmpty(self):
        '''Check if the head stack is empty.'''
        # Check if self.__head is none,
        # if it is, the queue is empty
        if self.__head.isEmpty():
            return True
        return False

def isPalindrome(s):
    '''Use your Queue and Stack class to test wheather an input is a palindrome.'''
    # Set up empty stack and queue
    myStack = Stack()
    myQueue = Queue()

    # Normalize string
    normal_s = s.upper()

    # Add letters if they are not spaces
    for letter in normal_s:
        if not letter == " ":
            myStack.push(letter)
            myQueue.enqueue(letter)

    # If queue and stack is empty, then invalid string
    if myQueue.isEmpty() and myStack.isEmpty():
        return False

    # Test whether it is palindrome by checking if letters match,
    # which should work as queue dequeues from the front of the word
    # while stack pops from the back of the word
    while not myQueue.isEmpty() and not myStack.isEmpty():
        comp1 = myQueue.dequeue()
        comp2 = myStack.pop()
        if not comp1 == comp2:
            return False
    return True

def isPalindromeEC(s):
    '''Implement if you wish to do the extra credit.'''
    '''Use your Queue and Stack class to test if an input is a palindrome.'''
    # Set up empty stack and queue
    myStack = Stack()
    myTSQueue = TwoStackQueue()

    # Normalize string
    normal_s = s.upper()

    # Add letters if they are not spaces
    for letter in normal_s:
        if not letter == " ":
            myStack.push(letter)
            myTSQueue.enqueue(letter)

    # If queue and stack is empty, then invalid string
    if myTSQueue.isEmpty() and myStack.isEmpty():
        return False

    # Test whether it is palindrome by checking if letters match,
    # which should work as queue dequeues from the front of the word
    # while stack pops from the back of the word
    while not myTSQueue.isEmpty() and not myStack.isEmpty():
        comp1 = myTSQueue.dequeue()
        comp2 = myStack.pop()
        if not comp1 == comp2:
            return False
    return True

