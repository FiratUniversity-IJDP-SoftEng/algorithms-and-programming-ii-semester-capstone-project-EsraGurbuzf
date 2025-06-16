# app.py (Updated for step-by-step visualization)

import streamlit as st
import matplotlib.pyplot as plt
from algorithm import kruskal 
from utils import draw_graph 

st.set_page_config(layout="wide") 

st.title("Kruskal's Minimum Spanning Tree Visualizer") 
st.write("Visualize the process of constructing a Minimum Spanning Tree (MST) using Kruskal's algorithm for a weighted graph, including the forest merging process.")

# --- Graph Data Definition (User Input) ---
st.header("1. Graph Data Input")

# Allow user to input number of nodes
num_nodes = st.number_input("Enter the number of nodes:", min_value=2, value=5, step=1)

st.write("**Enter Edges (Weight, Node1, Node2):**")
st.write("Enter one edge per line. Example: `10,0,1` (weight 10, between node 0 and 1)")

# Text area for edge input
edge_input = st.text_area("Edges:", value="10,0,1\n15,0,2\n12,1,3\n18,2,3\n20,1,4\n16,3,4")

# Parse edges from text area
edges = []
for line in edge_input.strip().split('\n'):
    if line:
        try:
            parts = line.split(',')
            if len(parts) == 3:
                weight = int(parts[0].strip())
                u = int(parts[1].strip())
                v = int(parts[2].strip())
                # Basic validation for node numbers
                if 0 <= u < num_nodes and 0 <= v < num_nodes:
                    edges.append((weight, u, v))
                else:
                    st.warning(f"Invalid node number in edge '{line}'. Nodes must be between 0 and {num_nodes-1}.")
            else:
                st.warning(f"Invalid format for edge '{line}'. Expected 'weight,node1,node2'.")
        except ValueError:
            st.warning(f"Could not parse edge '{line}'. Please check format.")

if not edges:
    st.warning("Please enter at least one edge to visualize the graph.")
    st.stop() # Stop execution if no edges are provided

st.write(f"**Parsed Edges:** {edges}")

# --- Visualize the Original Graph ---
st.subheader("Original Graph:")
original_graph_fig = draw_graph(num_nodes, edges, title="Original Graph")
st.pyplot(original_graph_fig)
plt.close(original_graph_fig)

# --- Kruskal's Algorithm Execution and Step-by-Step Visualization ---
st.header("2. Kruskal's Algorithm Step-by-Step Visualization")

# Run Kruskal's algorithm to get the steps
mst_edges, total_weight, steps = kruskal(num_nodes, edges)

# Slider to control the steps
if steps:
    # Adjust max_value for slider to include all steps
    step_index = st.slider("Select Step", 0, len(steps) - 1, 0)
    current_step_data = steps[step_index]

    st.subheader(f"Current Step: {step_index + 1} / {len(steps)}")
    st.info(current_step_data["description"])

    # Visualize the graph at the current step
    step_fig = draw_graph(
        n_nodes=num_nodes, 
        all_edges=edges, 
        highlighted_edges=current_step_data["current_mst_edges"], # MST edges built so far
        title=f"Step {step_index + 1}: {current_step_data['description']}",
        dsu_parent_state=current_step_data["dsu_state"], # Pass DSU state for component coloring
        processed_edge=current_step_data["processed_edge"] # Highlight currently processed edge
    )
    st.pyplot(step_fig)
    plt.close(step_fig)

    # Display final MST details after the steps
    if step_index == len(steps) - 1: # Only show final results on the last step
        st.subheader("Final Minimum Spanning Tree (MST):")
        if mst_edges:
            for u, v, w in mst_edges:
                st.write(f"Edge: ({u}, {v}), Weight: {w}")
            st.success(f"**Total MST Weight:** {total_weight}")
        else:
            st.warning("No MST found for this graph. It might be disconnected.")
else:
    st.warning("No steps generated. Check graph input or algorithm.")


st.markdown("---")
st.caption("Fırat University Software Engineering - Algorithm and Programming II Capstone Project")