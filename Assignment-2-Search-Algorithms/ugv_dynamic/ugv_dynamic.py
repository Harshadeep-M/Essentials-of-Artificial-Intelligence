import heapq
import random
import time
import matplotlib.pyplot as plt


GRID_SIZE = 70

DYNAMIC_OBSTACLES = 35
SENSOR_RANGE = 3
MAX_STEPS = 2000


def heuristic(node, goal):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])


def get_neighbors(node):
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
        ):
            neighbors.append((new_row, new_col))

    return neighbors


def a_star(start, goal, blocked):
    open_list = []

    heapq.heappush(
        open_list,
        (heuristic(start, goal), 0, start)
    )

    g_cost = {start: 0}
    parent = {start: None}

    while open_list:
        _, current_cost, current = heapq.heappop(open_list)

        if current_cost != g_cost[current]:
            continue

        if current == goal:
            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()
            return path

        for neighbor in get_neighbors(current):

            if neighbor in blocked:
                continue

            new_cost = current_cost + 1

            if (
                neighbor not in g_cost
                or new_cost < g_cost[neighbor]
            ):
                g_cost[neighbor] = new_cost
                parent[neighbor] = current

                f_cost = new_cost + heuristic(
                    neighbor,
                    goal
                )

                heapq.heappush(
                    open_list,
                    (f_cost, new_cost, neighbor)
                )

    return None


def move_dynamic_obstacles(obstacles, start, goal):
    new_positions = set()

    for obstacle in obstacles:
        possible_moves = [obstacle]

        for neighbor in get_neighbors(obstacle):
            if neighbor != start and neighbor != goal:
                possible_moves.append(neighbor)

        new_position = random.choice(possible_moves)

        if (
            new_position != start
            and new_position != goal
            and new_position not in new_positions
        ):
            new_positions.add(new_position)
        else:
            new_positions.add(obstacle)

    return new_positions


def detect_obstacles(position, obstacles):
    row, col = position

    detected = set()

    for obstacle in obstacles:
        obstacle_row, obstacle_col = obstacle

        distance = (
            abs(row - obstacle_row)
            + abs(col - obstacle_col)
        )

        if distance <= SENSOR_RANGE:
            detected.add(obstacle)

    return detected


def display_result(path, dynamic_obstacles, start, goal):
    plt.figure(figsize=(8, 8))

    if dynamic_obstacles:
        rows = [position[0] for position in dynamic_obstacles]
        cols = [position[1] for position in dynamic_obstacles]

        plt.scatter(
            cols,
            rows,
            marker="s",
            s=20,
            label="Dynamic Obstacles"
        )

    if path:
        rows = [position[0] for position in path]
        cols = [position[1] for position in path]

        plt.plot(
            cols,
            rows,
            linewidth=2,
            label="UGV Path"
        )

    plt.scatter(
        start[1],
        start[0],
        marker="o",
        s=100,
        label="Start"
    )

    plt.scatter(
        goal[1],
        goal[0],
        marker="X",
        s=100,
        label="Goal"
    )

    plt.title("UGV Navigation with Dynamic Obstacles")
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.legend()
    plt.grid(False)
    plt.show()


def main():
    print("UGV Dynamic Environment")
    print("=" * 35)

    start_input = input(
        "Enter start coordinates (row,col) "
        "or press Enter for (0,0): "
    ).strip()

    goal_input = input(
        "Enter goal coordinates (row,col) "
        "or press Enter for (69,69): "
    ).strip()

    if start_input:
        start = tuple(
            map(int, start_input.split(","))
        )
    else:
        start = (0, 0)

    if goal_input:
        goal = tuple(
            map(int, goal_input.split(","))
        )
    else:
        goal = (69, 69)

    random.seed(42)

    all_cells = [
        (row, col)
        for row in range(GRID_SIZE)
        for col in range(GRID_SIZE)
        if (row, col) != start
        and (row, col) != goal
    ]

    dynamic_obstacles = set(
        random.sample(
            all_cells,
            DYNAMIC_OBSTACLES
        )
    )

    known_obstacles = set()

    current = start
    complete_path = [current]

    replans = 0
    detected_obstacles = set()
    steps = 0

    start_time = time.perf_counter()

    while current != goal and steps < MAX_STEPS:

        # Dynamic obstacles move before each UGV action
        dynamic_obstacles = move_dynamic_obstacles(
            dynamic_obstacles,
            current,
            goal
        )

        # UGV detects only obstacles within sensor range
        newly_detected = detect_obstacles(
            current,
            dynamic_obstacles
        )

        detected_obstacles.update(newly_detected)
        known_obstacles.update(newly_detected)

        # Re-plan using the currently known obstacles
        path = a_star(
            current,
            goal,
            known_obstacles
        )

        replans += 1

        if path is None:
            # No currently known route.
            # Move one step after the environment changes.
            steps += 1
            continue

        if len(path) > 1:
            next_position = path[1]

            # Check whether a newly moved obstacle
            # blocks the next step.
            if next_position in dynamic_obstacles:
                steps += 1
                continue

            current = next_position
            complete_path.append(current)

        steps += 1

    execution_time = time.perf_counter() - start_time

    path_found = current == goal

    print("\nResult")
    print("-" * 35)
    print(f"Path Found: {path_found}")
    print(f"Path Length: {len(complete_path) - 1} km")
    print(f"Steps: {steps}")
    print(f"Re-planning Operations: {replans}")
    print(f"Obstacles Detected: {len(detected_obstacles)}")
    print(f"Execution Time: {execution_time:.6f} seconds")

    print("\nUGV Path:")
    print(complete_path)

    display_result(
        complete_path,
        dynamic_obstacles,
        start,
        goal
    )


if __name__ == "__main__":
    main()