class LinkedList():
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=None):
        self.start=elements[0]
        self.end=elements[-1]
        self.elements=elements
        return self

    def __str__(self):
        return str(self.elements)

    def __len__(self):
        return len(self.elements)

    def __iter__(self):
        pass

    def __getitem__(self, index):
        pass

    def __add__(self, other):
        return self.elements.append(other.elements)

    def __iadd__(self, other):
        return self.elements.append(other.elements)

    def __eq__(self, other):
        return all(x==y for x,y in zip(self.elements,other.elements))

    def append(self, elem):
        self.elements=elements.append(elem)
        return self

    def count(self):
        return count(self)

    def pop(self, index=None):
        if index==None:
            return self.elements.pop()
        else:
            return self.elements.pop(index)
