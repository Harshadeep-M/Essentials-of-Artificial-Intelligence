def is_valid(district, color, assignment, adjacency):
    """
    Check whether assigning a color to a district
    violates the coloring constraint.
    """

    for neighbor in adjacency[district]:
        if neighbor in assignment:
            if assignment[neighbor] == color:
                return False

    return True


def select_unassigned_variable(domains, assignment, adjacency):
    """
    Select the next district using the MRV heuristic.
    If two districts have the same domain size,
    choose the one with more neighbors.
    """

    unassigned = [
        district
        for district in domains
        if district not in assignment
    ]

    return min(
        unassigned,
        key=lambda district: (
            len(domains[district]),
            -len(adjacency[district])
        )
    )


def backtracking_search(domains, assignment, adjacency):
    """
    Find a valid graph coloring using backtracking.
    """

    # All districts have been assigned a color
    if len(assignment) == len(domains):
        return assignment.copy()

    district = select_unassigned_variable(
        domains,
        assignment,
        adjacency
    )

    for color in domains[district]:

        if is_valid(
            district,
            color,
            assignment,
            adjacency
        ):

            assignment[district] = color

            result = backtracking_search(
                domains,
                assignment,
                adjacency
            )

            if result is not None:
                return result

            # Backtrack
            del assignment[district]

    return None