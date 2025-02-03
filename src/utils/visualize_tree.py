import networkx as nx
import matplotlib.pyplot as plt

def visualize_tree(tree, fig, ax, pause_time=1):


    plt.clf()

    G = nx.Graph()
    pos = {}

    def add_nodes(node, x=0, y=0, layer = 1):

        if not node:
            return
        
        node_value = node.value

        G.add_node(node_value)
        pos[node_value] = (x,y)
        
        offset = 1 / (2 ** layer)

        left, right = node.left, node.right

        if left:
            G.add_edge(node.value, left.value)
            add_nodes(left, x - offset, y - 1, layer + 1)
        if right:
            G.add_edge(node.value, right.value)
            add_nodes(right, x + offset, y - 1, layer + 1)
    
    add_nodes(tree.root)

    nx.draw_networkx_nodes(G, pos,
        node_color = 'gray',
        node_size = 2000,
        node_shape = 'o')

    nx.draw_networkx_edges(G, pos,
        edge_color = 'gray',
        width = 2)
    
    nx.draw_networkx_labels(G, pos,
        font_size = 16,
        font_weight = 'bold')
    
    plt.axis('off')
    fig.canvas.draw()
    plt.pause(pause_time)



