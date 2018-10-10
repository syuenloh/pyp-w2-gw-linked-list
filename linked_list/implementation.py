class LinkedList():
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self,elements=None):
        self.elements=elements
        self.start = None
        self.end = None
        if elements:
            self.start=Node(elements[0],next=Node(elements[1]))
            self.end=Node(elements[-1])
            for elem in elements:
                self.append(elem)

    def __str__(self):
        return str(self.elements)

    def __len__(self):
        return len(self.elements)

    def __iter__(self):
        pass

    def __getitem__(self, index):
        return self.elements[index]

    def __add__(self, other):
        return self.elements.append(other.elements)

    def __iadd__(self, other):
        return self.elements.append(other.elements)

    def __eq__(self, other):
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        else:
            return self.elements==other.elements
        
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
        return len(self.elements)
    
    def __repr__(self):
        return "LinkedList({})".format(self.elements)

    def pop(self, index=None):
        if index==None:
            return self.elements.pop()
        else:
            return self.elements.pop(index)
