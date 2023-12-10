import networkx as nx
import matplotlib.pyplot as plt

"""
Using networkx and matplotlib to visualise output of ukkonens
"""

def draw_suffix_tree(string, root):
    # Create a simple graph
    graph = nx.Graph()

    labels = {}

    recursive_node_draw(string, graph, root, labels)

    # Draw the graph with node labels
    pos = nx.drawing.nx_pydot.graphviz_layout(graph, prog="twopi", root=0)
    nx.draw(graph, pos, with_labels=True, labels=labels, font_weight='bold', node_size=700, node_color='skyblue',
            font_color='black', font_size=8)
    plt.show()


def recursive_node_draw(string, graph, root, labels):
    for node in root.children.values():
        graph.add_node(node.id)
        labels[node.id] = f"[{string[node.start:node.end+1]}], [{node.start},{node.end}]"
        graph.add_edge(root.id, node.id)
        if root.suffix_link is not None:
            graph.add_edge(root.id, root.suffix_link.id, style="dashed")
        recursive_node_draw(string, graph, node, labels)