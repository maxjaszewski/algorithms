class Node:
    """
    Data structure used by Binomial Heap representation
    """
    # ID for drawing
    global_id = 0

    def __init__(self, key):
        self.id = Node.global_id
        Node.global_id += 1
        self.parent = None
        self.key = key
        self.child = None
        self.sibling = None
        self.degree = 0
