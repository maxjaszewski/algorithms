from binomial_heap import BinomialHeap
import networkx as nx
import matplotlib.pyplot as plt


def draw_binomial_heap(heap):
    graph, labels = nx.MultiDiGraph(), {}
    curr = heap.head
    while curr is not None:
        draw_binomial_tree(curr, graph, labels)
        curr = curr.sibling
    pos = nx.drawing.nx_pydot.graphviz_layout(graph, prog="twopi", root=0)
    nx.draw_networkx(graph, pos, with_labels=True, labels=labels, font_weight='bold', node_size=300,
                     node_color='skyblue',
                     font_color='black', font_size=8, edgelist=[])
    edge_styles = nx.get_edge_attributes(graph, 'style')
    parent_edges = [edge for edge, style in edge_styles.items() if style == 'p']
    nx.draw_networkx_edges(graph, pos, edgelist=parent_edges, edge_color='red', width=1, connectionstyle='arc3, rad = 0.25')
    child_edges = [edge for edge, style in edge_styles.items() if style == 'c']
    nx.draw_networkx_edges(graph, pos, edgelist=child_edges, edge_color='black', width=1, connectionstyle='arc3, rad = 0.3')
    sibling_edges = [edge for edge, style in edge_styles.items() if style == 's']
    nx.draw_networkx_edges(graph, pos, edgelist=sibling_edges, edge_color='blue', width=1)


    plt.show()

def draw_binomial_tree(node, graph, labels):
    graph.add_node(node.id)
    labels[node.id] = node.key
    if node.parent:
        graph.add_edge(node.id, node.parent.id, style="p")
    if node.child:
        graph.add_edge(node.id, node.child.id, style="c")
        draw_binomial_tree(node.child, graph, labels)
    if node.sibling:
        graph.add_edge(node.id, node.sibling.id, style="s")
        draw_binomial_tree(node.sibling, graph, labels)


if __name__ == "__main__":
    heap = BinomialHeap()
    heap.insert(10)
    heap.insert(20)
    heap.insert(5)
    heap.insert(30)
    draw_binomial_heap(heap)
