# Dijkstra's Algorithm — India Road Network

## Objective

The objective of this part of the assignment is to implement Dijkstra's algorithm on a road network containing cities in India and the distances between them.

The cities are represented as nodes in a graph, while the road distances are represented as edge weights.

## Dataset

The road-distance data is stored in `india_road_distances.csv`.

The dataset contains Indian cities, their connected cities, and the corresponding road distances in kilometres.

The dataset was obtained from an open-source dataset and is included in this project for implementing the search algorithm.

## Implementation

The program performs the following steps:

1. Reads the city and road-distance information from the CSV file.
2. Creates a weighted graph using the cities and their connections.
3. Uses Dijkstra's algorithm to calculate the shortest distances.
4. Stores the previous city for each shortest path.
5. Reconstructs and displays the shortest path between the starting city and every reachable city.

## Running the Program

From the project root directory, run:

```bash
python dijkstra_india/dijkstra.py