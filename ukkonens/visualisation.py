import networkx as nx
import matplotlib.pyplot as plt

"""
Using networkx and matplotlib to visualise output of ukkonens
"""

def visualise(suffix_tree):

    graph_labels = {
        "remainder": suffix_tree.remainder,
        "active_node": suffix_tree.active_node.id,
        "active_edge": suffix_tree.string[suffix_tree.active_edge] if suffix_tree.active_edge else "none",
        "active_length": suffix_tree.active_length,
    }
    plt.clf()
    # Create a simple graph
    graph = nx.Graph()
    labels = {}
    recursive_node_draw(suffix_tree.string, graph, suffix_tree.root, labels)
    # Draw the graph with node labels
    pos = nx.drawing.nx_pydot.graphviz_layout(graph, prog="dot", root=0)
    nx.draw_networkx(graph, pos, with_labels=True, labels=labels, font_weight='bold', node_size=700, node_color='skyblue',
            font_color='black', font_size=8, edgelist=[])
    edge_styles = nx.get_edge_attributes(graph, 'style')
    dashed_edges = [edge for edge, style in edge_styles.items() if style == 'link']
    solid_edges = [edge for edge, style in edge_styles.items() if style != 'link']
    nx.draw_networkx_edges(graph, pos, edgelist=dashed_edges, edge_color='red', style='dashed', width=2)
    nx.draw_networkx_edges(graph, pos, edgelist=solid_edges, edge_color='black', width=1)
    text = "\n".join(f"{key}: {value}" for key, value in graph_labels.items())
    plt.text(1.10, 1.10, text, horizontalalignment='right', verticalalignment='top', transform=plt.gca().transAxes)
    plt.show()


def recursive_node_draw(string, graph, root, labels):
    for node in root.children.values():
        graph.add_node(node.id)
        labels[node.id] = f"{node.id}\n{string[node.start:node.end+1]}, [{node.start},{node.end}]"
        graph.add_edge(root.id, node.id, style="standard")
        if root.suffix_link is not None:
            graph.add_edge(root.id, root.suffix_link.id, style="link")
        recursive_node_draw(string, graph, node, labels)