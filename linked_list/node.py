class Node(object):
    """
    Node class representing each of the linked nodes in the list.
    """

    def __init__(self, elem,next=None):
        self.elem=elem
        self.next=next
        
    def __str__(self):
        if self.next==None:
            return "Node({}) > /".format(self.elem)
        else:
            return "Node({}) > Node({})".format(self.elem,self.next.elem)

    def __eq__(self, other):
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        else:
            return self.elem==other.elem

    def __repr__(self):
        if self.next==None:
            return "Node({}) > /".format(self.elem)
        else:
            return "Node({}) > Node({})".format(self.elem,self.next.elem)
        
