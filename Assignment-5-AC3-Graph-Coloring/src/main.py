import json
import os

from ac3 import ac3
from graph_coloring import backtracking_search


def load_data():
    """Load Telangana district data from the JSON file."""

    base_dir = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )

    data_file = os.path.join(
        base_dir,
        "data",
        "telangana_districts.json"
    )

    with open(data_file, "r", encoding="utf-8") as file:
        return json.load(file)


def create_domains(districts, colors):
    """Create the initial color domain for every district."""

    return {
        district: colors.copy()
        for district in districts
    }


def verify_coloring(assignment, adjacency):
    """Verify that no adjacent districts have the same color."""

    for district in adjacency:
        for neighbor in adjacency[district]:

            if assignment[district] == assignment[neighbor]:
                return False

    return True


def main():

    data = load_data()

    districts = data["districts"]
    colors = data["colors"]
    adjacency = data["adjacency"]

    print("=" * 60)
    print("TELANGANA DISTRICT GRAPH COLORING")
    print("AC-3 + CSP BACKTRACKING")
    print("=" * 60)

    print(f"\nTotal districts : {len(districts)}")
    print(f"Available colors: {colors}")

    # --------------------------------------------------
    # STEP 1: Create CSP domains
    # --------------------------------------------------

    domains = create_domains(districts, colors)

    print("\nInitial domains created.")
    print("Each district initially has colors:", colors)

    # --------------------------------------------------
    # STEP 2: Apply AC-3
    # --------------------------------------------------

    print("\nRunning AC-3...")

    consistent = ac3(domains, adjacency)

    if not consistent:
        print("CSP is inconsistent. No solution exists.")
        return

    print("AC-3 completed successfully.")

    # --------------------------------------------------
    # STEP 3: Graph Coloring using Backtracking
    # --------------------------------------------------

    print("\nFinding valid graph coloring...")

    assignment = backtracking_search(
        domains,
        {},
        adjacency
    )

    if assignment is None:
        print("No valid coloring found.")
        return

    # --------------------------------------------------
    # STEP 4: Display result
    # --------------------------------------------------

    print("\nValid coloring found!\n")

    for district in sorted(assignment):
        print(
            f"{district:30} -> Color {assignment[district]}"
        )

    # --------------------------------------------------
    # STEP 5: Verify solution
    # --------------------------------------------------

    valid = verify_coloring(
        assignment,
        adjacency
    )

    print("\n" + "=" * 60)

    if valid:
        print("RESULT: VALID GRAPH COLORING")
    else:
        print("RESULT: INVALID GRAPH COLORING")

    print("=" * 60)


if __name__ == "__main__":
    main()