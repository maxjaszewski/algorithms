class Node:
    """
    Data structure used by Binomial Heap representation
    """
    def __init__(self, key):
        self.parent = None
        self.key = None
        self.child = None
        self.sibling = None
        self.degree = None
