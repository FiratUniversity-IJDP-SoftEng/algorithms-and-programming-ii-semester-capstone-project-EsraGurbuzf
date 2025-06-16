# utils.py (Updated for DSU state visualization and highlighting)

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np # Needed for color mapping

def draw_graph(n_nodes, all_edges, highlighted_edges=None, 
               title="Graph Visualization", path_to_highlight=[],
               dsu_parent_state=None, # New parameter for DSU state
               processed_edge=None): # New parameter for the currently processed edge

    G = nx.Graph()
    G.add_nodes_from(range(n_nodes))

    nx_edges_with_weights = []
    for w, u, v in all_edges:
        nx_edges_with_weights.append((u, v, {'weight': w}))
    G.add_edges_from(nx_edges_with_weights)

    pos = nx.spring_layout(G, seed=42) # Consistent layout

    fig, ax = plt.subplots(figsize=(10, 8))

    # Determine node colors based on DSU parent state (components)
    node_colors = ['lightblue'] * n_nodes # Default color
    if dsu_parent_state:
        # Map roots to unique colors
        unique_roots = sorted(list(set([dsu_parent_state[i] for i in range(n_nodes)])))
        color_map = plt.cm.get_cmap('tab10', len(unique_roots)) # 'tab10' is a good colormap for categories
        
        # Create a mapping from root to color index
        root_to_color_idx = {root: idx for idx, root in enumerate(unique_roots)}

        # Assign colors to nodes based on their root
        node_colors = [color_map(root_to_color_idx[dsu_parent_state[i]]) for i in range(n_nodes)]
    
    # Draw nodes with dynamic colors
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=700, ax=ax)
    nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold', ax=ax)

    # Draw all edges (grey and thin by default)
    all_edge_list = [(u, v) for w, u, v in all_edges]
    nx.draw_networkx_edges(G, pos, edgelist=all_edge_list, edge_color='gray', width=1, ax=ax)
    
    # Draw edge labels (weights) for all edges
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', ax=ax)

    # Highlight specific edges (e.g., MST edges) if provided
    if highlighted_edges:
        highlight_list = [(u, v) for u, v, w in highlighted_edges]
        nx.draw_networkx_edges(G, pos, edgelist=highlight_list, edge_color='green', width=3, ax=ax)
    
    # Highlight the currently processed edge
    if processed_edge:
        u_proc, v_proc, w_proc = processed_edge
        nx.draw_networkx_edges(G, pos, edgelist=[(u_proc, v_proc)], edge_color='orange', width=4, style='solid', ax=ax)
        # Optionally, draw a specific label for the processed edge
        nx.draw_networkx_edge_labels(G, pos, edge_labels={(u_proc, v_proc): f'Current ({w_proc})'}, 
                                     font_color='orange', font_weight='bold', ax=ax)


    ax.set_title(title)
    ax.axis('off')
    
    return fig