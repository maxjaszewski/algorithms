import networkx as nx
import matplotlib.pyplot as plt
from disjoint_set import DisjointSet

def draw_disjoint_set(dj):
    plt.clf()
    graph = nx.DiGraph()
    for i in range(len(dj.parent)):
        graph.add_node(i)
        graph.add_edge(i, dj.parent[i])
    pos = nx.drawing.nx_pydot.graphviz_layout(graph, prog="twopi")
    nx.draw(graph, pos, with_labels=True)
    plt.show()


if __name__ == "__main__":
    dj = DisjointSet(20)
    for i in range(0, 20, 2):
        dj.union(i, i + 1)
    dj.union(3,4)
    dj.union(4,5)
    dj.union(13, 14)
    dj.union(14,15)
    dj.union(14, 3)
    draw_disjoint_set(dj)

