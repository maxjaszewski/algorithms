from node import Node as Node

class BinomialTree():

    def __init__(self, is_empty, value):
        self.head = Node(value)
        self.is_empty = is_empty
        self.order = 0

    def merge(self, tree):

        # Check same order
        if self.order != tree.order:
            raise Exception(f"Trying to merge tree of order {self.order} with tree of order {tree.order}")



        x = self.head.key
        y = tree.head.key

        if x <= y:
            tree.head.parent = self.head
            self.head.degree += 1
            if self.head.child:
                tree.head.sibling = self.head.child
            # head remains unchanged
        else:
            self.head.parent = tree.head
            tree.head.degree += 1
            if tree.head.child:
                self.head.sibling = tree.head.child
            self.head = tree.head

        self.order += 1
