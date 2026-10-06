# UGV Navigation in a Dynamic Environment

## Objective

The objective of this part of the assignment is to modify the UGV navigation problem so that the obstacles are dynamic and are not completely known in advance.

Unlike the static environment, the UGV has to detect obstacles while moving, update its knowledge of the environment, and re-plan its route when necessary.

## Approach

A* Search is used for path planning.

The UGV does not initially know the complete obstacle map. Instead, it uses a limited sensor range to detect nearby obstacles.

When obstacles are detected, they are added to the UGV's known-obstacle map. A* is then used again to calculate a route from the UGV's current position to the goal.

The dynamic obstacles are also allowed to move during the simulation.

## Environment

The grid size is:

**70 × 70 km**

Default start position:

**(0, 0)**

Default goal position:

**(69, 69)**

The program also allows the user to enter different start and goal coordinates.

## Dynamic Obstacle Handling

The simulation follows these steps:

1. Generate dynamic obstacles in the environment.
2. Start the UGV from the selected starting position.
3. Move the dynamic obstacles.
4. Detect obstacles within the UGV's sensor range.
5. Add detected obstacles to the known-obstacle map.
6. Run A* from the UGV's current position to the goal.
7. Move the UGV one step along the calculated path.
8. Repeat the process until the goal is reached.

This allows the UGV to react to changes in the environment instead of relying on a completely known map.

## Sensor Model

The UGV uses a limited sensing range of:

**3 grid cells**

Only obstacles within this range are detected and added to the known obstacle information.

## Measures of Effectiveness

The following measures are recorded:

1. **Path Found** - Whether the UGV successfully reached the goal.
2. **Path Length** - Total distance travelled by the UGV.
3. **Steps** - Number of movement steps performed.
4. **Re-planning Operations** - Number of times the path was recalculated.
5. **Obstacles Detected** - Number of dynamic obstacles detected during navigation.
6. **Execution Time** - Time taken by the simulation.

## Result

For the tested environment:

| Measure | Result |
|---|---:|
| Path Found | Yes |
| Path Length | 138 km |
| Steps | 138 |
| Re-planning Operations | 138 |
| Obstacles Detected | 17 |
| Execution Time | 0.708287 seconds |

The UGV successfully reached the goal while operating in an environment containing dynamic obstacles.

The simulation performed path planning repeatedly as the UGV moved and detected obstacles.

## Visualization

The generated visualization shows:

- The dynamic obstacles
- The UGV path
- The starting position
- The goal position

The path demonstrates how the UGV navigates through the environment while responding to obstacle information obtained during movement.

## Running the Program

From the project root directory, run:

```bash
python ugv_dynamic/ugv_dynamic.py