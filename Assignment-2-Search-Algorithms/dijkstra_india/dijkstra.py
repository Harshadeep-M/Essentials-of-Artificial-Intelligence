import csv
import heapq


def load_graph(filename):
    graph = {}

    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            origin = row["Origin"].strip()
            destination = row["Destination"].strip()
            distance = float(row["Distance"])

            if origin not in graph:
                graph[origin] = {}

            if destination not in graph:
                graph[destination] = {}

            graph[origin][destination] = distance
            graph[destination][origin] = distance

    return graph


def dijkstra(graph, start):
    distances = {city: float("inf") for city in graph}
    previous = {city: None for city in graph}

    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_city = heapq.heappop(priority_queue)

        if current_distance > distances[current_city]:
            continue

        for neighbor, road_distance in graph[current_city].items():
            new_distance = current_distance + road_distance

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current_city

                heapq.heappush(
                    priority_queue,
                    (new_distance, neighbor)
                )

    return distances, previous


def get_path(previous, start, destination):
    path = []
    current = destination

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    if path[0] != start:
        return []

    return path


def main():
    filename = "dijkstra_india/india_road_distances.csv"

    graph = load_graph(filename)

    print("Available cities:")
    print(", ".join(sorted(graph.keys())))

    start = input("\nEnter starting city: ").strip()

    if start not in graph:
        print("City not found in the dataset.")
        return

    distances, previous = dijkstra(graph, start)

    print(f"\nShortest distances from {start}:\n")

    for city in sorted(distances):
        if distances[city] == float("inf"):
            print(f"{city}: Not reachable")
        else:
            path = get_path(previous, start, city)
            print(
                f"{city}: {distances[city]:.0f} km"
                f" | Path: {' -> '.join(path)}"
            )


if __name__ == "__main__":
    main()