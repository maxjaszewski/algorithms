from visualise import visualise


class Node:
    # ID used in algorithm to check if root or not
    id = 0
    # static variable to increment all leaves end point
    # when extending
    leaf_end = -1

    def __init__(self, is_leaf: bool):
        self.id = Node.id
        Node.id += 1
        self.children = {}
        self.is_leaf = is_leaf
        self.start = None
        self.end = None
        self.suffix_link = None

    def __getattribute__(self, item):
        # override end to use dynamic global leaf end for leaves
        if item == "end":
            if self.is_leaf:
                return Node.leaf_end
        # default behaviour
        return object.__getattribute__(self, item)

    def __eq__(self, node):
        # Use instance id to identify nodes
        return self.id == node.id


class SuffixTree:
    def __init__(self):
        self.last_new_node = None
        self.active_node = Node(False)
        self.active_edge = -1
        self.active_length = 0
        self.remainder = 0
        self.root = None
        self.string = ""
        self.size = 0

    def build(self, data: str):
        self.string = data + "$"
        self.size = len(self.string)
        self.root = self.create_node(-1, -1, False)
        # self.root.suffix_link = self.root  # Root has start and end -1
        self.active_node = self.root
        for i in range(self.size):
            self.extend(i)
            visualise(self, i)

    def create_node(self, start, end, is_leaf):
        node = Node(is_leaf)
        node.start = start
        node.end = end
        return node

    def position(self, i):
        if (self.active_length == 0):
            self.active_edge = i
        elif self.active_node.children[self.string[self.active_edge]].start + self.active_length - 1 >= \
                self.active_node.children[self.string[self.active_edge]].end and not \
                self.active_node.children[self.string[self.active_edge]].is_leaf:
            start = self.active_node.children[self.string[self.active_edge]].start
            end = self.active_node.children[self.string[self.active_edge]].end
            diff = end - start + 1
            self.active_node = self.active_node.children[self.string[self.active_edge]]
            self.active_length -= diff
            self.active_edge = self.active_edge + diff
            self.position(i)

    def extend(self, i: int):
        # update leaf end global with extension
        Node.leaf_end = i
        # increment remainder as extra suffix to be added
        self.remainder += 1
        self.last_new_node = None
        # loop continues while inserting remaining suffixes
        # continue or break if match found and going to next char
        while self.remainder > 0:
            # Follow active length to position
            self.position(i)

            # no matching edge, create new leaf
            if self.active_node.children.get(self.string[self.active_edge]) is None:
                self.active_node.children[self.string[self.active_edge]] = self.create_node(start=i, end=None,
                                                                                            is_leaf=True)
            # matching edge
            else:
                # next character is matching break to next i
                if self.string[self.active_node.children[self.string[self.active_edge]].start + self.active_length] == \
                        self.string[i]:
                    self.active_length += 1
                    break

                # next character mismatch, must split
                curr_pos = self.active_node.children[self.string[self.active_edge]].start + self.active_length
                # new intermediate node
                split_node = self.create_node(
                    start=self.active_node.children[self.string[self.active_edge]].start,
                    end=curr_pos - 1,
                    is_leaf=False)
                # organise children of node
                split_node.children[self.string[curr_pos]] = self.active_node.children[self.string[self.active_edge]]
                split_node.children[self.string[i]] = self.create_node(
                    start=i,
                    end=None,
                    is_leaf=True)
                self.active_node.children[self.string[self.active_edge]].start = curr_pos
                # repoint to split node
                self.active_node.children[self.string[self.active_edge]] = split_node

                # update suffix link if new node has already been inserted
                if self.last_new_node:
                    self.last_new_node.suffix_link = split_node
                # update last new node for next suffix link
                self.last_new_node = split_node

                # directing where to next
                if self.active_node == self.root:
                    self.active_edge = i - self.remainder + 2
                    self.active_length -= 1
                elif self.active_node.suffix_link is not None:
                    self.active_node = self.active_node.suffix_link
                else:
                    self.active_node = self.root

            # at this point have inserted split/leaf
            self.remainder -= 1


if __name__ == "__main__":
    suffix_tree = SuffixTree()
    suffix_tree.build("abcabmabn")
