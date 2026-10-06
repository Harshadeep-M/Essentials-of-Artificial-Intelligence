# Uninformed Search Techniques

## 1. Breadth-First Search (BFS)

### Definition
Breadth-First Search explores the search space level by level. It expands all nodes at the current depth before moving to nodes at the next depth.

### Strategy
BFS uses a **FIFO (First-In, First-Out) queue** to store the frontier nodes.

### Completeness
BFS is complete if the branching factor is finite.

### Optimality
BFS is optimal when all actions have the same cost.

### Time Complexity
O(b^d)

### Space Complexity
O(b^d)

Where:
- **b** = branching factor
- **d** = depth of the shallowest goal

### Applications
- Finding the shortest path in an unweighted graph
- Network traversal
- Web crawling
- Finding minimum-hop routes

## 2. Depth-First Search (DFS)

### Definition
Depth-First Search explores one branch of the search space as deeply as possible before going back and exploring another branch.

### Strategy
DFS uses a **LIFO (Last-In, First-Out) stack**. It can also be implemented using recursion.

### Completeness
DFS is not complete in general because it can get stuck exploring a very deep or infinite branch.

### Optimality
DFS is not optimal because it may find a longer path even when a shorter path exists.

### Time Complexity
O(b^m)

### Space Complexity
O(bm)

Where:
- **b** = branching factor
- **m** = maximum depth of the search tree

### Applications
- Maze solving
- Graph traversal
- Topological sorting
- Detecting cycles in graphs
## 3. Uniform-Cost Search (UCS)

### Definition
Uniform-Cost Search expands the node with the lowest total path cost from the starting node. Unlike BFS, it can handle situations where different actions have different costs.

### Strategy
UCS uses a **priority queue**, where nodes are ordered according to their path cost.

The evaluation function is:

**f(n) = g(n)**

where **g(n)** is the cost of the path from the start node to node n.

### Completeness
UCS is complete when every step has a positive cost.

### Optimality
UCS is optimal because it always expands the node with the lowest path cost first.

### Time Complexity
O(b^(1 + floor(C*/ε)))

### Space Complexity
O(b^(1 + floor(C*/ε)))

Where:
- **b** = branching factor
- **C*** = cost of the optimal solution
- **ε** = minimum cost of an action

### Applications
- Finding the least-cost route between locations
- Network routing
- Road and transportation networks
- Problems where different actions have different costs

## 3. Uniform-Cost Search (UCS)

### Definition
Uniform-Cost Search expands the node with the lowest total path cost from the starting node. It is useful when different actions or paths have different costs.

### Strategy
UCS uses a priority queue to keep track of the nodes that need to be explored. The node with the lowest path cost is selected first.

The evaluation function is:

**f(n) = g(n)**

where **g(n)** is the total cost of the path from the starting node to node n.

### Completeness
UCS is complete when the cost of every action is greater than zero.

### Optimality
UCS is optimal because it expands the node with the lowest path cost first, so it can find the least-cost solution.

### Time Complexity
O(b^(1 + floor(C*/ε)))

### Space Complexity
O(b^(1 + floor(C*/ε)))

Where:
- **b** = branching factor
- **C*** = cost of the optimal solution
- **ε** = minimum cost of an action

### Applications
- Finding the least-cost route between cities
- Road and transportation networks
- Network routing
- Problems where different actions have different costs

## 4. Depth-Limited Search (DLS)

### Definition
Depth-Limited Search is a modified version of Depth-First Search where a maximum depth is fixed in advance. The search does not explore nodes beyond this limit.

### Strategy
DLS follows a depth-first approach but stops expanding a branch when the specified depth limit is reached.

### Completeness
DLS is complete if the depth limit is greater than or equal to the depth of the shallowest goal.

### Optimality
DLS is not optimal because it may find a solution that is not the shortest or least-cost solution.

### Time Complexity
O(b^l)

### Space Complexity
O(bl)

Where:
- **b** = branching factor
- **l** = depth limit

### Applications
- Searching problems where the maximum search depth is known
- Avoiding infinite paths in depth-first search
- Game trees with a fixed search depth
- Situations where exploring very deep paths is unnecessary

## 5. Iterative Deepening Search (IDS)

### Definition
Iterative Deepening Search combines the ideas of Depth-First Search and Breadth-First Search. It repeatedly performs a depth-limited search, increasing the depth limit by one each time until the goal is found.

### Strategy
IDS starts with a depth limit of 0 and gradually increases it:

- Depth 0
- Depth 1
- Depth 2
- Depth 3
- And so on until the goal is found

### Completeness
IDS is complete when the branching factor is finite.

### Optimality
IDS is optimal when all actions have the same cost.

### Time Complexity
O(b^d)

### Space Complexity
O(bd)

Where:
- **b** = branching factor
- **d** = depth of the shallowest goal

### Applications
- Searching large state spaces
- Problems where the depth of the solution is unknown
- Situations where memory is limited
- Puzzle-solving problems


## 6. Bidirectional Search

### Definition
Bidirectional Search searches from both the initial state and the goal state at the same time. The two searches continue until they meet at a common node.

### Strategy
One search starts from the initial node and another starts from the goal node. Instead of searching the entire space from one direction, both searches explore smaller portions of the search space.

### Completeness
Bidirectional Search can be complete when the individual searches are complete and the search conditions allow the two searches to meet.

### Optimality
It can be optimal when used with an appropriate optimal search strategy, such as BFS, and when all step costs are equal.

### Time Complexity
O(b^(d/2))

### Space Complexity
O(b^(d/2))

Where:
- **b** = branching factor
- **d** = depth of the solution

### Applications
- Finding shortest paths in graphs
- Road and transportation networks
- Network routing
- Problems where both the start and goal states are known


# Comparison of Uninformed Search Techniques

| Technique | Strategy | Data Structure | Complete | Optimal | Time Complexity | Space Complexity |
|---|---|---|---|---|---|---|
| BFS | Explores level by level | Queue | Yes* | Yes* | O(b^d) | O(b^d) |
| UCS | Expands lowest-cost path | Priority Queue | Yes* | Yes | O(b^(1 + floor(C*/ε))) | O(b^(1 + floor(C*/ε))) |
| DFS | Explores deepest branch first | Stack | No | No | O(b^m) | O(bm) |
| DLS | DFS with a depth limit | Stack | Yes** | No | O(b^l) | O(bl) |
| IDS | Repeated depth-limited search | Stack | Yes* | Yes* | O(b^d) | O(bd) |
| Bidirectional | Searches from both ends | Depends on search | Yes** | Yes** | O(b^(d/2)) | O(b^(d/2)) |

**Notes:**
- `*` depends on the search conditions, such as finite branching or equal step costs.
- `**` depends on the chosen depth limit and whether the two searches can meet.
- **b** = branching factor
- **d** = depth of the shallowest goal
- **m** = maximum depth of the search tree
- **l** = depth limit
- **C*** = cost of the optimal solution
- **ε** = minimum action cost