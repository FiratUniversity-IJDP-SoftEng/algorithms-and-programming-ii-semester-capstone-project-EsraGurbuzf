# Kruskal's Algorithm - Interactive MST Visualizer

## Project Overview

This project is an interactive web application that implements and visualizes **Kruskal's Algorithm for Minimum Spanning Tree (MST)**, developed as part of the Algorithms and Programming II course at Fırat University, Software Engineering Department. It aims to provide a clear, step-by-step understanding of how Kruskal's algorithm constructs an MST, particularly focusing on the forest merging process using the Disjoint Set Union (DSU) data structure.

## Algorithm Description


### Problem Definition

The problem addressed is finding the **Minimum Spanning Tree (MST)** of a **connected, weighted, undirected graph**. An MST is a subset of the edges of a connected, edge-weighted undirected graph that connects all the vertices together, without any cycles and with the minimum possible total edge weight.

### Mathematical Background

Kruskal's algorithm relies on the **Cut Property** and the **Cycle Property** of MSTs:
* **Cut Property:** For any cut (a partition of the vertices into two disjoint sets), if an edge has a strictly smaller weight than any other edge crossing the cut, then this edge belongs to all MSTs of the graph.
* **Cycle Property:** If $C$ is a cycle in the graph, and $e$ is an edge of $C$ with a larger weight than any other edge of $C$, then $e$ cannot belong to an MST.

The **Disjoint Set Union (DSU)** data structure is fundamental to the algorithm's efficiency, allowing for quick checks on whether adding an edge creates a cycle.

### Algorithm Steps

1.  **Initialization:**
    * Create an empty set `MST_Edges` to store the edges of the Minimum Spanning Tree.
    * For each vertex in the graph, create a separate disjoint set using a DSU data structure. Initially, each vertex is its own component (forest).
2.  **Sort Edges:** Sort all edges of the graph in non-decreasing order of their weights.
3.  **Iterate and Connect:**
    * Iterate through the sorted edges, from the smallest weight to the largest.
    * For each edge $(u, v)$ with weight $w$:
        * **Check for Cycle:** Use the `find` operation of the DSU to determine if vertices $u$ and $v$ already belong to the same connected component (set).
        * **Add to MST (if no cycle):** If `find(u)` and `find(v)` return different roots (meaning $u$ and $v$ are in different components), it implies adding this edge will not form a cycle. Add $(u, v, w)$ to `MST_Edges`.
        * **Merge Components:** Perform a `union` operation on the sets containing $u$ and $v$ to merge them into a single component.
        * **Skip Edge (if cycle):** If `find(u)` and `find(v)` return the same root, it means adding this edge would create a cycle. Discard this edge.
4.  **Termination:** The algorithm terminates when `MST_Edges` contains $V-1$ edges (where $V$ is the number of vertices), or when all edges have been processed.
### Pseudocode

```
Function Kruskal(vertices V, edges E):
    MST_Edges = empty list
    Sort E by weight in non-decreasing order

    Initialize DSU_structure with |V| sets (each vertex in its own set)

    For each edge (u, v) with weight w in sorted E:
        If DSU_structure.Find(u) is not equal to DSU_structure.Find(v):
            Add (u, v, w) to MST_Edges
            DSU_structure.Union(u, v)
        If len(MST_Edges) == |V| - 1: // Using len() for list size check
            Break (MST is complete)
            
    Return MST_Edges
```

## Complexity Analysis

### Time Complexity

-   **Best Case:** $O(E \log E)$ - [Explanation: The dominant factor in Kruskal's algorithm is the initial sorting of all $E$ edges. Even in the best-case scenario (e.g., edges are already sorted, or the graph is very sparse), this sorting operation still takes $O(E \log E)$ time. The subsequent DSU operations ($find$ and $union$), even with optimizations, contribute an amortized $O(E \alpha(V))$ which is practically constant time and thus typically dwarfed by the sorting.]
-   **Average Case:** $O(E \log E)$ - [Explanation: For most general graph inputs, the sorting of edges will be the most time-consuming part. The Disjoint Set Union (DSU) operations, with their amortized nearly constant time ($O(\alpha(V))$ per operation), do not change this dominant factor. Therefore, the average case remains $O(E \log E)$.]
-   **Worst Case:** $O(E \log E)$ - [Explanation: Similar to the average and best cases, the worst-case time complexity is also dominated by the sorting of edges, which is $O(E \log E)$. While DSU operations theoretically can approach a slightly higher complexity than constant per operation (e.g., if path compression is not optimally used across all calls), for practical purposes and with Union by Rank and Path Compression, the $O(E \log E)$ for sorting remains the tightest upper bound for overall performance.]

### Space Complexity

-   $O(V + E)$ - [Explanation: The space complexity stems from several components: $O(V)$ for the Disjoint Set Union (DSU) data structure's parent and rank arrays (where $V$ is the number of vertices), $O(E)$ for storing the input graph's edges, and $O(V)$ for the list of edges in the Minimum Spanning Tree (MST), which can contain at most $V-1$ edges. For the interactive visualization feature, an additional $O(E \cdot V)$ space is used to store snapshots of the DSU state at each step; this is an overhead for visualization and not part of the core algorithm's inherent space needs.]

## Features

-   **Kruskal's Algorithm Implementation:** A robust and accurate implementation of Kruskal's algorithm for finding the Minimum Spanning Tree (MST).
-   **Optimized Disjoint Set Union (DSU):** Utilizes key DSU optimizations like **Path Compression** and **Union by Rank** for efficient set operations and cycle detection.
-   **Interactive Graph Input:** Allows users to easily define graphs by specifying the number of nodes and entering custom edges with their weights.
-   **Step-by-Step Visualization:** Provides a clear, animated walkthrough of the algorithm's execution, highlighting the currently processed edge, edges added to the MST, and dynamically colored nodes representing disjoint sets.
-   **Dynamic Node Coloring:** Visualizes the merging of components (disjoint sets) through distinct node colors at each step, making the DSU process intuitive.
-   **Detailed Step Descriptions:** Offers clear textual explanations for each algorithmic step, describing why an edge is chosen or skipped (e.g., "Edge added, components merged" or "Cycle detected, edge skipped").
-   **Original and Final MST Visualizations:** Displays both the initial state of the input graph and the final computed Minimum Spanning Tree with its total weight.
-   **User-Friendly Interface:** Built with Streamlit, providing an intuitive and interactive web-based application.
-   **Comprehensive Testing:** Includes unit tests to ensure the correctness and robustness of the algorithm and DSU implementation.

## Screenshots

![Main Interface](docs/screenshots/main_interface.png)
*Caption describing the main interface*

![Algorithm in Action](docs/screenshots/algorithm_demo.png)
*Caption describing the algorithm in action*

## Installation

### Prerequisites

-   Python 3.8 or higher
-   Git

### Setup Instructions

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/FiratUniversity-IJDP-SoftEng/algorithms-and-programming-ii-semester-capstone-project-EsraGurbuzf.git]
    cd algorithms-and-programming-ii-semester-capstone-project-EsraGurbuzf
    ```

2.  **Create a virtual environment (Recommended):**
    ```bash
    # On Windows
    python -m venv venv
    venv\Scripts\activate

    # On macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    *(First, ensure you have a `requirements.txt` file in your project root by running `pip freeze > requirements.txt` if you haven't already created it.)*
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application:**
    ```bash
    streamlit run app.py
    ```
    Your default web browser will automatically open a new tab with the Kruskal's MST Visualizer application.

### Usage Guide

1.  After running `streamlit run app.py`, the application will open in your default web browser.
2.  In the "Graph Data Input" section, enter the desired number of nodes.
3.  In the "Enter Edges" text area, input graph edges in the format `weight,node1,node2` (e.g., `10,0,1`), one edge per line. Node numbers should be 0-indexed and within the specified number of nodes.
    * **My Learning Point:** Parsing user input correctly from a string like "10,0,1" into a `(weight, u, v)` tuple for processing was a small but crucial detail. It required the use of Python's string methods like `.strip()` (to remove extra spaces), `.split(',')` (to break the string by commas), and `int()` (to convert string parts to integers).
4.  The "Original Graph" will be displayed immediately based on your input.
5.  Navigate through the algorithm's execution steps using the "Select Step" slider in the "Kruskal's Algorithm Step-by-Step Visualization" section. Observe how edges are considered, MST is built, and components merge (indicated by node colors).
    * **My Learning Point:** The dynamic node coloring based on DSU state was a significant visual feature I worked on. It involved capturing the `dsu_parent_state` (the internal representation of which node belongs to which set) at each step of the algorithm and then using this data in the `draw_graph` utility function to assign unique colors to nodes belonging to the same component, making the merging process very clear.
6.  The final MST edges and total weight will be displayed at the end of the steps.

### Example Inputs

Here's an example graph you can use to test the application:

* **Number of Nodes:** `5`
* **Edges Input:**
    ```
    10,0,1
    15,0,2
    12,1,3
    18,2,3
    20,1,4
    16,3,4
    ```
* **Expected Output (Total MST Weight):** `53` (The exact set of edges may vary if multiple MSTs with the same total weight exist, but the minimum total weight will be consistent.)

## Implementation Details

### Key Components

-   `algorithm.py`: Contains the core implementation of the `DSU` (Disjoint Set Union) class with Path Compression and Union by Rank optimizations, and the `kruskal` algorithm function itself. This file encapsulates the fundamental logic of the MST computation.
-   `app.py`: This is the main Streamlit application script. It handles the user interface (UI) elements for input and output, orchestrates the calls to the `kruskal` function, and uses `utils.py` to render the various graph visualizations and manage the step-by-step playback.
-   `utils.py`: Provides helper functions, primarily `draw_graph`, which utilizes `matplotlib` and `networkx` libraries to draw the graph visualizations. It includes logic for highlighting edges, coloring nodes based on their DSU component state, and displaying edge weights.
-   `test_algorithm.py`: A dedicated unit test file that employs Python's `unittest` framework to verify the correctness and robustness of the `kruskal` algorithm and the `DSU` implementation under various graph scenarios.

### Code Highlights

This section highlights some key code snippets that form the core of the Kruskal algorithm's implementation and its visualization infrastructure.

#### DSU `union` Method: The Heart of Cycle Detection (from `algorithm.py`)

The `union` method within the `DSU` class is central to Kruskal's algorithm, as it efficiently determines if adding an edge creates a cycle and merges disjoint sets. Its `True` or `False` return value is crucial for deciding whether an edge can be included in the MST.

```python
# Excerpt from algorithm.py
class DSU:
    # ... (init and find methods) ...

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            # Union by Rank optimization: attach smaller tree under larger tree's root
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_j] < self.rank[root_i]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
            return True # Successful merge: edge can be added to MST
        return False  # Cycle detected: edge cannot be added to MST

## Testing

This project includes a comprehensive unit test suite to verify the correctness and robustness of the algorithm implementation:

```bash
python -m unittest test_algorithm.py
```

### Test Cases

The `test_algorithm.py` file includes various test cases designed to cover different scenarios and edge cases for Kruskal's algorithm and the Disjoint Set Union (DSU) implementation:

-   **`test_basic_connected_graph`**: Validates the algorithm's functionality on a standard, fully connected graph with distinct edge weights, ensuring it correctly finds the MST.
-   **`test_disconnected_graph`**: Checks the behavior when the input graph is not fully connected. The algorithm should correctly identify that a spanning tree cannot connect all vertices and stop when all reachable components are connected.
-   **`test_graph_with_cycle`**: Confirms that the algorithm correctly identifies and skips edges that would form a cycle, thus upholding the MST property.
-   **`test_single_node_graph`**: Tests edge cases with a graph containing only a single node (where MST should be empty).
-   **`test_graph_with_no_edges`**: Verifies handling of graphs with multiple nodes but no connecting edges (resulting in an empty MST).
-   **`test_duplicate_weights`**: Ensures correct processing when multiple edges share the same weight, confirming that a valid MST (though potentially not unique in terms of edge set) is still found.
-   **`test_dsu_operations`**: Specific tests for the `DSU` class to ensure `find` (with path compression) and `union` (with union by rank) operations work as expected for various merge scenarios.

## Live Demo

A live demo of this application is available at: [[Insert Streamlit Cloud URL here](https://kruskalgorithm.streamlit.app/)]

## Limitations and Future Improvements

### Current Limitations

-   **Static Graph Input:** Currently, graph edges are entered via a text area. There's no interactive drawing or drag-and-drop functionality for creating graphs directly on the visualization canvas.
-   **Limited Graph Layouts:** The visualization primarily uses NetworkX's `spring_layout` for node positioning. There are no readily available options for alternative graph layouts (e.g., circular, planar) which might be more suitable for certain graph structures.
-   **Basic Input Validation:** While basic validation exists for numerical inputs and format, more robust error handling for malformed edge inputs (e.g., non-numeric weights, non-integer node IDs, or incorrectly formatted lines) could be implemented to provide clearer user feedback.
-   **No Dynamic Graph Manipulation:** Users cannot add or remove edges/nodes dynamically *after* the initial graph input has been processed. To change the graph, the input must be entirely re-entered.
-   **Performance for Very Large Graphs:** For extremely large graphs (hundreds or thousands of nodes/edges), the visualization might experience performance slowdowns due to rendering overhead within Streamlit and Matplotlib/NetworkX.

### Planned Improvements

-   **Interactive Graph Editor:** Implement features to allow users to draw/edit graphs directly on the canvas, providing a more intuitive and engaging way to define graph structures. This could include adding nodes, drawing edges, and moving nodes.
-   **Export Functionality:** Provide options to download the generated MST data (e.g., as a CSV or JSON file containing edges and total weight) or the current graph visualization as an image (e.g., PNG, SVG).
-   **Alternative Layout Algorithms:** Offer choices for different graph layout algorithms (e.g., circular, planar, Kamada-Kawai) to allow users to experiment with various visual representations of their graphs.
-   **Enhanced Edge/Node Information Display:** Add hover-over tooltips or a dedicated sidebar panel to display detailed information about selected edges (e.g., its state in the algorithm: processed, in MST, skipped) or nodes (e.g., its current component ID).
-   **Performance Optimizations for Large Graphs:** Investigate and implement strategies to improve rendering performance for very large datasets, potentially by optimizing drawing routines or considering more efficient visualization libraries if bottlenecks persist.
-   **In-App Algorithm Information:** Expand the "Algorithm Description" section directly within the Streamlit application interface itself for quick reference, rather than only in the `README.md`.

## References and Resources

This project benefited from a variety of academic and online resources that deepened my understanding of Kruskal's algorithm, graph theory, and web application development with Streamlit.

### Academic References

1.  **Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to Algorithms* (3rd ed.). MIT Press.**
    *(This highly acclaimed textbook was a primary reference for a deep understanding of Kruskal's Algorithm, the properties of Minimum Spanning Trees, and the intricate details of the Disjoint-Set Data Structures, particularly chapters focusing on graph algorithms and DSU.)*
2.  **Goodrich, M. T., & Tamassia, R. (2014). *Algorithm Design: Foundations, Analysis, and Internet Examples* (2nd ed.). John Wiley & Sons.**
    *(Another valuable resource consulted for alternative perspectives on algorithm design principles and graph theory concepts.)*
3.  **Skiena, S. S. (2008). *The Algorithm Design Manual* (2nd ed.). Springer.**
    *(Provided practical insights into implementing graph algorithms and common pitfalls, complementing the theoretical knowledge.)*

### Online Resources

#### Streamlit Specific Resources
-   **Streamlit Documentation:** The official documentation was essential for learning how to build interactive web applications with Streamlit in Python, covering core functionalities and advanced features.
    * [https://docs.streamlit.io/](https://docs.streamlit.io/)
-   **Streamlit Components:** Explored the Streamlit Components gallery to understand how custom components can extend application functionality.
    * [https://streamlit.io/components](https://streamlit.io/components)
-   **Streamlit Deployment:** Utilized Streamlit's deployment guides for deploying the application to Streamlit Cloud.
    * [https://docs.streamlit.io/cloud](https://docs.streamlit.io/cloud)

#### General Algorithm Resources
-   **GeeksforGeeks - Kruskal's Algorithm:** A widely used online platform that provided clear explanations and various code examples for Kruskal's algorithm, aiding in the initial understanding and implementation.
    * [https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/](https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/)
-   **GeeksforGeeks - Disjoint Set Union (DSU):** Provided detailed insights into the Disjoint Set Union data structure, including explanations of Path Compression and Union by Rank optimizations, which were critical for efficient implementation.
    * [https://www.geeksforgeeks.org/disjoint-set-union-union-by-rank-and-path-compression/](https://www.geeksforgeeks.org/disjoint-set-union-union-by-rank-and-path-compression/)
-   **VisuAlgo:** An excellent online tool for visualizing various algorithms, including Kruskal's, which significantly helped in conceptualizing the step-by-step visualization logic for this project.
    * [https://visualgo.net](https://visualgo.net)
-   **Algorithm Visualizations (University of San Francisco):** Another valuable resource for animated algorithm explanations, offering different perspectives on how algorithms operate.
    * [https://www.cs.usfca.edu/~galles/visualization/Algorithms.html](https://www.cs.usfca.edu/~galles/visualization/Algorithms.html)

## Author

- **Name:** [Esra Gürbüz]
- **Student ID:** [230543001]
- **GitHub:** [EsraGurbuzf]

## Acknowledgements

I would like to thank Assoc. Prof. Ferhat UÇAR for his invaluable guidance and support throughout this project, particularly in clarifying complex algorithmic concepts and providing a robust academic framework.

---

*This project was developed as part of the Algorithms and Programming II course at Fırat University, Technology Faculty, Software Engineering Department.*
