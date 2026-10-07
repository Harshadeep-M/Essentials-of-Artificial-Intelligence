import json
import os

from ac3 import ac3
from graph_coloring import backtracking_search


def load_data():
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


def test_assignment():
    data = load_data()

    districts = data["districts"]
    colors = data["colors"]
    adjacency = data["adjacency"]

    # Check 33 districts
    assert len(districts) == 33

    # Create domains
    domains = {
        district: colors.copy()
        for district in districts
    }

    # AC-3 must succeed
    assert ac3(domains, adjacency) is True

    # Find coloring
    assignment = backtracking_search(
        domains,
        {},
        adjacency
    )

    # A solution must exist
    assert assignment is not None

    # Every district must be assigned
    assert len(assignment) == 33

    # Only allowed colors can be used
    for color in assignment.values():
        assert color in colors

    # Adjacent districts must have different colors
    for district in adjacency:
        for neighbor in adjacency[district]:
            assert assignment[district] != assignment[neighbor]

    print("All Assignment 5 tests passed!")


if __name__ == "__main__":
    test_assignment()