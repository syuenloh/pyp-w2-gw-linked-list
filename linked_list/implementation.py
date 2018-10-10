class LinkedList():
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self,elements=None):
        self.elements=elements
        self.start = None
        self.end = None
        if elements:
            for elem in elements:
                self.append(elem)
        else:
            elements=[]

    def __str__(self):
        if self.elements:
            return str(self.elements)
        else:
            return "[]"

    def __len__(self):
        if self.elements:
            return len(self.elements)
        else:
            return 0

    def __iter__(self):
        pass

    def __getitem__(self, index):
        if self.elements:
            return self.elements[index]
        else:
            raise IndexError

    def __add__(self, other):
        if self.elements is not None and other.elements is not None:
            for elem in reversed(self.elements):
                other.elements=[elem]+other.elements
            return other
        elif other.elements is None:
            return self
        else:
            return other

    def __iadd__(self, other):
        if self.elements is not None and other.elements is not None:
            for elem in reversed(self.elements):
                other.elements=[elem]+other.elements
            return other
        elif other.elements is None:
            return self
        else:
            return other

    def __eq__(self, other):
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        else:
            self.elements==other.elements
        
    def append(self, elem):
        new_node = Node(elem)
        if self.start is None:
            self.start = new_node
            self.end = self.start
            self.elements=[elem]
        else:
            self.end.next = new_node
            self.end = new_node
            self.elements.append(elem)

    def count(self):
        if self.elements:
            return len(self.elements)
        else:
            return 0
    
    def __repr__(self):
        return "LinkedList({})".format(self.elements)

    def pop(self, index=None):
        if index==None:
            return self.elements.pop()
        else:
            return self.elements.pop(index)