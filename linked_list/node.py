class Node(object):
    """
    Node class representing each of the linked nodes in the list.
    """

    def __init__(self, elem):
        self.elem=elem
        self.next=None
        
    def __str__(self):
        if self.next != None:
            return "Node({}) > Node ({})".format(self.elem,self.next)
        else:
            return "Node({}) > /".format(self.elem)

    def __eq__(self, other):
        return self.elem==other.elem

    def __repr__(self):
        if self.next != None:
            return "Node({}) > Node ({})".format(self.elem,self.next)
        else:
            return "Node({}) > /".format(self.elem)
