# Search Algorithms Assignment

## Assignment 2

This project covers uninformed search, informed search, heuristic techniques, Dijkstra's algorithm, and UGV path planning in static and dynamic environments.

---

# 1. Uninformed Search Techniques

Uninformed search techniques do not use additional information about how close a state is to the goal. They mainly use the structure of the search problem to decide which node should be explored next.

The following techniques are compared:

- Breadth-First Search (BFS)
- Uniform-Cost Search (UCS)
- Depth-First Search (DFS)
- Depth-Limited Search (DLS)
- Iterative Deepening Search (IDS)
- Bidirectional Search

The comparison considers:

- Search strategy
- Data structure used
- Completeness
- Optimality
- Time complexity
- Space complexity
- Typical applications

The detailed comparison is available in:

`uninformed_search/comparison.md`

---

# 2. Informed Search Techniques

Informed search techniques use additional information about the problem, usually in the form of a heuristic, to guide the search toward the goal.

The techniques covered in this assignment are:

- Greedy Best-First Search
- Best-First Search
- Dijkstra's Algorithm
- A* Algorithm
- Beam Search
- Recursive Best-First Search (RBFS)
- Iterative Deepening A* (IDA*)
- Weighted A*

The detailed explanation and possible applications are available in:

`informed_search/informed_search.md`

---

# 3. Heuristics

A heuristic is an estimate of the remaining cost from a current state to a goal state.

This section covers:

- Satisficing search
- Admissible heuristics
- Formulating a heuristic for a search problem
- Generating heuristics from subproblems

The detailed explanation is available in:

`informed_search/heuristics.md`

---

# 4. Programming Assignment

## 4.1 Dijkstra's Algorithm on an Indian Road Network

A weighted graph representing a set of Indian cities and their road distances was used.

Each city is represented as a node and each road connection is represented as an edge with its distance as the edge cost.

Dijkstra's algorithm was implemented to calculate the shortest distance from a user-specified starting city to all reachable cities in the dataset.

### Input

The user specifies the starting city.

Example:

```text
Enter starting city: Delhi