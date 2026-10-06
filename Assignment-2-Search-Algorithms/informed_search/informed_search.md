# Informed Search Techniques

Informed search techniques use additional information about the problem to decide which states should be explored first. This additional information is usually represented by a heuristic function.

## 1. Greedy Best-First Search

### Definition
Greedy Best-First Search selects the node that appears to be closest to the goal according to the heuristic value.

### Evaluation Function

**f(n) = h(n)**

where **h(n)** estimates the cost from node n to the goal.

### Advantages
- Can reach the goal quickly when the heuristic is good.
- Usually explores fewer nodes than uninformed methods.

### Limitations
- It is not guaranteed to find the optimal solution.
- Its performance depends heavily on the quality of the heuristic.

### Applications
- Route finding
- Game navigation
- Robot navigation
- Pathfinding problems


## 2. Best-First Search

### Definition
Best-First Search is a general search strategy that selects the most promising node according to an evaluation function.

The evaluation function determines which node should be explored next.

Different versions of Best-First Search use different evaluation functions. For example, Greedy Best-First Search uses **h(n)**, while A* uses **g(n) + h(n)**.

### Applications
- Pathfinding
- Planning problems
- Game AI
- Search problems where some estimate of solution quality is available


## 3. Dijkstra's Algorithm

### Definition
Dijkstra's algorithm finds the shortest path from a starting node to other nodes in a weighted graph when all edge costs are non-negative.

In AI, this is closely related to Uniform-Cost Search because both expand the node with the lowest path cost.

### Evaluation Function

**f(n) = g(n)**

where **g(n)** is the cost of reaching node n from the starting node.

### Advantages
- Finds the shortest path when edge costs are non-negative.
- Works well for weighted graphs.

### Limitation
- It does not use a heuristic, so it may explore many unnecessary nodes.

### Applications
- Road networks
- Network routing
- Transportation systems
- Finding shortest paths in weighted graphs


## 4. A* Search

### Definition
A* Search combines the actual cost of reaching a node with an estimate of the remaining cost to the goal.

### Evaluation Function

**f(n) = g(n) + h(n)**

where:
- **g(n)** = cost from the start node to n
- **h(n)** = estimated cost from n to the goal

### Advantages
- Can find optimal solutions when an appropriate admissible heuristic is used.
- Usually explores fewer nodes than Dijkstra's algorithm when the heuristic provides useful information.

### Limitations
- Can require a large amount of memory.
- Its performance depends on the heuristic.

### Applications
- GPS and route planning
- Robot path planning
- Video game pathfinding
- Map navigation


## 5. Beam Search

### Definition
Beam Search is a search technique that keeps only a fixed number of the most promising nodes at each level of the search.

The fixed number is called the **beam width**.

For example, if the beam width is 3, only the three most promising nodes are kept for further exploration at each level.

### Advantages
- Uses less memory than many exhaustive search methods.
- Can be faster because it ignores less promising paths.

### Limitations
- It may discard the path leading to the best solution.
- It is not guaranteed to find an optimal solution.

### Applications
- Natural language processing
- Speech recognition
- Sequence generation
- Large search spaces where memory is limited


## 6. Recursive Best-First Search (RBFS)

### Definition
Recursive Best-First Search is a memory-efficient version of Best-First Search. It tries to follow the most promising path while keeping enough information to return and explore another path if necessary.

### Strategy
RBFS keeps track of the best alternative path and uses a limit on the evaluation value. If the current path becomes worse than the best alternative, the algorithm goes back and explores the alternative.

### Advantages
- Uses much less memory than standard A*.
- Can still use heuristic information to guide the search.

### Limitations
- May revisit nodes and therefore can take more time.
- Its performance depends on the heuristic.

### Applications
- AI planning
- Puzzle solving
- Pathfinding when memory is limited


## 7. Iterative Deepening A* (IDA*)

### Definition
IDA* combines the memory efficiency of Iterative Deepening Search with the heuristic guidance of A*.

Instead of using a fixed depth limit, it uses a limit based on the evaluation function:

**f(n) = g(n) + h(n)**

The limit is increased gradually until a solution is found.

### Advantages
- Requires much less memory than A*.
- Can find an optimal solution when the heuristic is admissible and the search conditions are appropriate.

### Limitations
- It may repeatedly explore the same nodes.
- Can become slow when the search space is large.

### Applications
- Puzzle solving
- Game search
- Pathfinding
- Problems where memory is limited


## 8. Weighted A*

### Definition
Weighted A* modifies the A* evaluation function by giving more importance to the heuristic estimate.

### Evaluation Function

**f(n) = g(n) + w × h(n)**

where **w > 1** is the weight applied to the heuristic.

### Advantages
- Can find solutions faster than standard A*.
- Useful when finding a good solution quickly is more important than guaranteeing the exact optimal solution.

### Limitations
- Increasing the weight can cause the algorithm to return a non-optimal solution.
- The result depends on the chosen weight and heuristic.

### Applications
- Real-time pathfinding
- Robotics
- Video games
- Large search problems where speed is important


# Summary of Informed Search Techniques

| Technique | Evaluation Function / Main Idea | Uses Heuristic? | Main Characteristic |
|---|---|---|---|
| Greedy Best-First | f(n) = h(n) | Yes | Chooses the node estimated closest to the goal |
| Best-First | Depends on evaluation function | Usually | General strategy for selecting the most promising node |
| Dijkstra | f(n) = g(n) | No | Finds the lowest-cost path |
| A* | f(n) = g(n) + h(n) | Yes | Combines actual cost and estimated remaining cost |
| Beam Search | Keeps a fixed number of best nodes | Yes | Reduces memory by limiting the search width |
| RBFS | Best-first with recursive memory management | Yes | Uses less memory than A* |
| IDA* | Iterative limits using f(n) = g(n) + h(n) | Yes | Combines iterative deepening with A* |
| Weighted A* | f(n) = g(n) + w × h(n) | Yes | Gives more importance to the heuristic |