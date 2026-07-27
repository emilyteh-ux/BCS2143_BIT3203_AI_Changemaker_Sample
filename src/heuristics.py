"""Heuristic functions for informed search."""

import math

from graph import CampusGraph


def straight_line_distance(graph: CampusGraph, node_id: str, goal_id: str) -> float:
    """Admissible heuristic: Euclidean distance never overestimates true walking distance
    on this map, since walking paths cannot be shorter than a straight line."""
    x1, y1 = graph.coordinates(node_id)
    x2, y2 = graph.coordinates(goal_id)
    return math.dist((x1, y1), (x2, y2))
