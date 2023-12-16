from node import Node as Node

class BinomialHeap:
    """
    Heap data structure for integers. Intention to be used as a priority queue.
    """
    def __init__(self):
        self.head = Node()

    def insert(self, key):
        """
        Create new node with key and insert
        :param key: value of key
        """
        pass

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

    def merge(self, heap):
        """
        Merge two binomial heaps
        :param heap: second heap
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

