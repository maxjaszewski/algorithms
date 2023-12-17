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
        heap = BinomialHeap()
        heap.head = Node(key)
        self.head = merge(self, heap)

    def min(self):
        """
        Get minimum key value
        :return: Node object
        """
        # Track the parent as well so min_node can be removed when extracting minimum value
        minimum, min_node, min_node_left = float('-inf'), None, None
        prev, curr = None, self.head
        while curr is not None:
            if curr.key < minimum:
                minimum, min_node, min_node_left = curr.key, curr, prev
            prev, curr = curr, curr.sibling
        return min_node, min_node_left

    def extract_min(self):
        """
        Get and remove minimum value
        :return: Node object
        """
        min_node, min_node_left = self.min()
        if min_node_left is None:
            self.head = min_node.sibling
        else:
            min_node_left.sibling = min_node.sibling

        children_heap = BinomialHeap()
        children_heap.head = min_node.child
        children_heap.reverse()
        self.head = union(self, children_heap).head

        min_node.child = None
        min_node.degree = None
        min_node.sibling = None
        return min_node

    def decrease_key(self, node, key):
        """
        Decreases key
        :param node: object to decrease
        :param key: new value
        """
        if key >= node.key:
            raise Exception("Cannot decrease key value to larger value")
        curr = node
        while node.parent and node.key < node.parent.key:
            curr.key = node.parent.key
        curr.key = key

    def delete(self, node):
        """
        Removes node
        :param node:
        """
        self.decrease_key(node, float('-inf'))
        self.extract_min()

    def reverse(self):
        curr = self.head
        new_start = None
        while curr is not None:
            snap_next = curr.sibling
            curr.sibling = new_start
            new_start = curr
            curr = snap_next
        self.head = new_start


"""
                                            -- FUNCTIONS --
"""


def merge(h1, h2):
    """
    Merge two binomial heaps into one linked list with roots in monotonically increasing order
    :param h1: Head of first binomial heap
    :param h2: Head of second binomial heap
    :return: Merged heap
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


def union(h1, h2):
    """
    Join two Binomial Heaps
    :param h1: First
    :param h2: Second
    :return: Union heap
    """
    res_heap = BinomialHeap()
    res_heap.head = merge(h1, h2).head
    if res_heap.head is None:
        return res_heap
    prev, curr, next = None, res_heap.head, res_heap.head.sibling
    while next is not None:
        if (curr.degree != next.degree) or (next.sibling and next.degree == next.sibling.degree):
            prev, curr, next = curr, next, next.sibling
        else:
            if curr.key <= next.key:
                curr.sibling = next.sibling
                link(next, curr)
            else:
                if prev is not None:
                    prev.sibling = next
                else:
                    res_heap.head = next
                link(curr, next)

    return res_heap
