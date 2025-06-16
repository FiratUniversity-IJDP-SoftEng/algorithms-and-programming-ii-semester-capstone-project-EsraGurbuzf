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

- **Best Case:** O(...) - [Explanation]
- **Average Case:** O(...) - [Explanation]
- **Worst Case:** O(...) - [Explanation]

### Space Complexity

- O(...) - [Explanation]

## Features

- [Feature 1]
- [Feature 2]
- [Feature 3]
...

## Screenshots

![Main Interface](docs/screenshots/main_interface.png)
*Caption describing the main interface*

![Algorithm in Action](docs/screenshots/algorithm_demo.png)
*Caption describing the algorithm in action*

## Installation

### Prerequisites

- Python 3.8 or higher
- Git

### Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/your-repository.git
   cd your-repository
   ```

2. Create a virtual environment:
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   streamlit run app.py
   ```

## Usage Guide

1. [Step 1 of using the application]
2. [Step 2 of using the application]
3. [Step 3 of using the application]
...

### Example Inputs

- [Example 1 with expected output]
- [Example 2 with expected output]
- [Example 3 with expected output]

## Implementation Details

### Key Components

- `algorithm.py`: Contains the core algorithm implementation
- `app.py`: Main Streamlit application
- `utils.py`: Helper functions for data processing
- `visualizer.py`: Functions for visualization

### Code Highlights

```python
# Include a few key code snippets that demonstrate the most important parts of your implementation
def key_function(parameter):
    """
    Docstring explaining what this function does
    """
    # Implementation with comments explaining the logic
    result = process(parameter)
    return result
```

## Testing

This project includes a test suite to verify the correctness of the algorithm implementation:

```bash
python -m unittest test_algorithm.py
```

### Test Cases

- [Test case 1 description]
- [Test case 2 description]
- [Test case 3 description]

## Live Demo

A live demo of this application is available at: [Insert Streamlit Cloud URL here]

## Limitations and Future Improvements

### Current Limitations

- [Limitation 1]
- [Limitation 2]
- [Limitation 3]

### Planned Improvements

- [Improvement 1]
- [Improvement 2]
- [Improvement 3]

## References and Resources

### Academic References

1. [Reference 1]
2. [Reference 2]
3. [Reference 3]

### Online Resources

- [Resource 1]
- [Resource 2]
- [Resource 3]

## Author

- **Name:** [Your Name]
- **Student ID:** [Your Student ID]
- **GitHub:** [Your GitHub Username]

## Acknowledgements

I would like to thank Assoc. Prof. Ferhat UÇAR for guidance throughout this project, and [any other acknowledgements].

---

*This project was developed as part of the Algorithms and Programming II course at Fırat University, Technology Faculty, Software Engineering Department.*
