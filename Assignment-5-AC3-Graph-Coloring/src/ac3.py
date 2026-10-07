from collections import deque


def revise(domains, district1, district2):
    """
    Remove values from district1's domain that have
    no compatible value in district2's domain.
    """

    revised = False

    for color in domains[district1].copy():

        supported = any(
            color != other_color
            for other_color in domains[district2]
        )

        if not supported:
            domains[district1].remove(color)
            revised = True

    return revised


def ac3(domains, adjacency):
    """
    AC-3 algorithm for enforcing arc consistency.
    """

    queue = deque()

    # Add every directed arc to the queue
    for district in adjacency:
        for neighbor in adjacency[district]:
            queue.append((district, neighbor))

    while queue:

        district1, district2 = queue.popleft()

        if revise(domains, district1, district2):

            # Empty domain means no solution
            if not domains[district1]:
                return False

            # Recheck affected neighbors
            for neighbor in adjacency[district1]:

                if neighbor != district2:
                    queue.append((neighbor, district1))

    return True