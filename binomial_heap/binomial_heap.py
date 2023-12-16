from node import Node as Node


class BinomialHeap:
    """
    Heap data structure for integers. Intention to be used as a priority queue.
    """

    def __init__(self):
        self.head = None

    def insert(self, key):
        """
        Create new node with key and insert
        :param key: value of key
        """
        heap = BinomialHeap(key)
        self.merge(heap)

    def min(self):
        """
        Get minimum key value
        :return: Node object
        """
        pass  # todo

    def extract_min(self):
        """
        Get and remove minimum value
        :return: Minimum integer
        """
        pass  # todo

    def decrease_key(self, node, key):
        """
        Decreases key
        :param node: object to decrease
        :param key: new value
        """
        if key >= node.key:
            raise Exception("Cannot decrease key value to larger value")
        # todo rest
        pass

    def delete(self, node):
        """
        Removes node
        :param node:
        """
        pass  # todo


"""
                                            -- FUNCTIONS --
"""


def union(h1, h2):
    """
    Join two Binomial Heaps
    :param h1: First
    :param h2: Second
    :return: Union heap
    """
    res_heap = BinomialHeap()
    res_heap.head = merge(h1, h2)
    prev, curr, next = None, res_heap.head, res_heap.head.sibling






def merge(h1, h2):
    """
    Merge two binomial heaps into one linked list with roots in monotonically increasing order
    :param h1: Head of first binomial heap
    :param h2: Head of second binomial heap
    :return:
    """
    p1, p2 = h1.head, h2.head
    curr, res = None, None

    # sort nodes into monotonically increasing order
    while p1 is not None and p2 is not None:
        if p1.key <= p2.key:
            # init
            if not curr and not res:
                curr, res = p1, p1
            else:
                curr.sibling = p1
                p1 = p1.sibling
        else:
            # init
            if not curr and not res:
                curr, res = p2, p2
            else:
                curr.sibling = p2
                p2 = p2.sibling
        # shift curr to sibling
        curr = curr.sibling

    # add remaining non-empty trees
    if p1 is not None:
        curr.sibling = p1
    else:
        curr.sibling = p2

    return res


def link(x, y):
    """
    Links two binomial trees. y becomes the root node
    :param y: Head of first Binomial Tree
    :param x: Head of second Binomial Tree
    """
    x.sibling = y.child
    y.degree += 1
    x.parent = y
    y.child = x
