import heapq
import random
import time
import matplotlib.pyplot as plt


GRID_SIZE = 70

START = (0, 0)
GOAL = (69, 69)

DENSITIES = {
    "Low": 0.15,
    "Medium": 0.25,
    "High": 0.35
}


def generate_grid(density, seed=42):
    random.seed(seed)

    grid = []

    for row in range(GRID_SIZE):
        current_row = []

        for col in range(GRID_SIZE):
            if random.random() < density:
                current_row.append(1)
            else:
                current_row.append(0)

        grid.append(current_row)

    # Keep start and goal free
    grid[START[0]][START[1]] = 0
    grid[GOAL[0]][GOAL[1]] = 0

    return grid


def heuristic(node, goal):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])


def get_neighbors(node, grid):
    row, col = node

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    neighbors = []

    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc

        if (
            0 <= new_row < GRID_SIZE
            and 0 <= new_col < GRID_SIZE
            and grid[new_row][new_col] == 0
        ):
            neighbors.append((new_row, new_col))

    return neighbors


def a_star(grid, start, goal):
    open_list = []

    heapq.heappush(
        open_list,
        (heuristic(start, goal), 0, start)
    )

    g_cost = {start: 0}
    parent = {start: None}

    nodes_explored = 0

    while open_list:
        _, current_cost, current = heapq.heappop(open_list)

        if current_cost != g_cost[current]:
            continue

        nodes_explored += 1

        if current == goal:
            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()

            return path, nodes_explored

        for neighbor in get_neighbors(current, grid):
            new_cost = g_cost[current] + 1

            if (
                neighbor not in g_cost
                or new_cost < g_cost[neighbor]
            ):
                g_cost[neighbor] = new_cost
                parent[neighbor] = current

                f_cost = new_cost + heuristic(neighbor, goal)

                heapq.heappush(
                    open_list,
                    (f_cost, new_cost, neighbor)
                )

    return None, nodes_explored


def calculate_measures(path, nodes_explored, execution_time):
    if path is None:
        return {
            "Path Found": False,
            "Path Length": 0,
            "Nodes Explored": nodes_explored,
            "Execution Time": execution_time
        }

    return {
        "Path Found": True,
        "Path Length": len(path) - 1,
        "Nodes Explored": nodes_explored,
        "Execution Time": execution_time
    }


def display_result(grid, path, density_name, measures):
    plt.figure(figsize=(8, 8))

    plt.imshow(grid, cmap="gray_r")

    if path:
        rows = [node[0] for node in path]
        cols = [node[1] for node in path]

        plt.plot(cols, rows, linewidth=2, label="UGV Path")

    plt.scatter(
        START[1],
        START[0],
        marker="o",
        s=100,
        label="Start"
    )

    plt.scatter(
        GOAL[1],
        GOAL[0],
        marker="X",
        s=100,
        label="Goal"
    )

    plt.title(
        f"UGV Path - {density_name} Obstacles\n"
        f"Path Length: {measures['Path Length']} | "
        f"Nodes Explored: {measures['Nodes Explored']}"
    )

    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.legend()
    plt.grid(False)
    plt.show()

def main():
    print("UGV Static Environment")
    print("=" * 30)

    for density_name, density in DENSITIES.items():

        print(f"\nTesting {density_name} obstacle density...")

        seed = 42

        while True:
            grid = generate_grid(density, seed)

            start_time = time.perf_counter()

            path, nodes_explored = a_star(
                grid,
                START,
                GOAL
            )

            execution_time = time.perf_counter() - start_time

            if path is not None:
                break

            seed += 1

        measures = calculate_measures(
            path,
            nodes_explored,
            execution_time
        )

        print(f"Path Found: {measures['Path Found']}")
        print(f"Path Length: {measures['Path Length']} km")
        print(f"Nodes Explored: {measures['Nodes Explored']}")
        print(f"Execution Time: {measures['Execution Time']:.6f} seconds")

        print("Path:")
        print(path)

        display_result(
            grid,
            path,
            density_name,
            measures
        )


if __name__ == "__main__":
    main()