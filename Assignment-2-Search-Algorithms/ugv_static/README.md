# UGV Navigation in a Static Environment

## Objective

The objective of this part of the assignment is to design an algorithm that allows an Unmanned Ground Vehicle (UGV) to navigate through a 70 × 70 km grid, avoid known obstacles, and reach a specified goal using the shortest possible path.

Three different obstacle densities are tested:

- Low: 15%
- Medium: 25%
- High: 35%

The obstacles are generated randomly before the search begins and remain static during navigation.

## Approach

A* Search is used for path planning because it combines the cost of reaching the current position with an estimate of the remaining distance to the goal.

The evaluation function is:

**f(n) = g(n) + h(n)**

For this grid, Manhattan distance is used as the heuristic:

**h(n) = |x₁ - x₂| + |y₁ - y₂|**

The UGV can move one cell at a time in four directions:

- Up
- Down
- Left
- Right

Diagonal movement is not allowed.

Each grid cell represents approximately 1 km, so the path length is reported in kilometres.

## Environment

The grid size is:

**70 × 70 km**

Start position:

**(0, 0)**

Goal position:

**(69, 69)**

Obstacle cells cannot be entered by the UGV.

## Obstacle Generation

Obstacles are generated randomly using three density levels:

| Density | Obstacle Percentage |
|---|---:|
| Low | 15% |
| Medium | 25% |
| High | 35% |

If a randomly generated environment does not contain a valid path between the start and goal, another environment is generated at the same density until a valid path is obtained.

## Measures of Effectiveness

The following measures are used to evaluate the UGV navigation:

1. **Path Found** - Whether the UGV was able to reach the goal.
2. **Path Length** - Total number of grid movements required to reach the goal.
3. **Nodes Explored** - Number of grid positions explored by A*.
4. **Execution Time** - Time taken by the search algorithm to find the path.

## Results

| Obstacle Density | Path Found | Path Length | Nodes Explored | Execution Time |
|---|---|---:|---:|---:|
| Low (15%) | Yes | 138 km | 3308 | 0.022888 s |
| Medium (25%) | Yes | 138 km | 1440 | 0.003940 s |
| High (35%) | Yes | 148 km | 1206 | 0.081152 s |

## Result Analysis

For the low and medium obstacle densities, the UGV was able to reach the goal using a path of 138 km.

The theoretical minimum distance between (0, 0) and (69, 69), when only horizontal and vertical movement is allowed, is:

**69 + 69 = 138 km**

Therefore, these two cases found a shortest possible path.

For the high obstacle density, the path length increased to 148 km because the UGV had to take additional movements to avoid the larger number of obstacles.

The number of nodes explored also changed with obstacle density. The algorithm explored 3308 nodes for the low-density environment, 1440 nodes for the medium-density environment, and 1206 nodes for the high-density environment.

Execution time also varied between the generated environments because the arrangement of obstacles affects the search space.

## Visualization

The program generates a visualization for each obstacle density showing:

- Obstacles
- Start position
- Goal position
- UGV path

The path is traced from the start position to the goal while avoiding all known static obstacles.

## Running the Program

From the project root directory, run:

```bash
python ugv_static/ugv_static.py