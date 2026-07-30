"""Search algorithms for the Accessible Campus Route Planner.

Two AI methods are implemented and compared, as required by the assignment brief:

1. `uniform_cost_search` — an uninformed baseline. It finds the shortest path by
   distance alone and does not consider accessibility.
2. `a_star_search` — the improved, principal method. It uses the straight-line-distance
   heuristic from heuristics.py and can enforce a wheelchair-accessibility constraint,
   which is the actual social-impact requirement of this project.

Both functions return a SearchResult so that path cost, nodes expanded and execution
time can be reported and compared, as required for the testing/results deliverable.
"""

from __future__ import annotations

import heapq
import time
from dataclasses import dataclass, field
from typing import Callable, List, Optional

from graph import CampusGraph


@dataclass
class SearchResult:
    path: Optional[List[str]]
    cost: float
    nodes_expanded: int
    execution_time_s: float

    @property
    def found(self) -> bool:
        return self.path is not None


def _reconstruct(came_from: dict, start: str, goal: str) -> List[str]:
    path = [goal]
    while path[-1] != start:
        path.append(came_from[path[-1]])
    path.reverse()
    return path


def uniform_cost_search(graph: CampusGraph, start: str, goal: str) -> SearchResult:
    """Baseline uninformed search (Dijkstra / UCS). Ignores accessibility."""
    t0 = time.perf_counter()
    frontier: list = [(0.0, start)]
    came_from: dict = {}
    best_cost = {start: 0.0}
    nodes_expanded = 0

    while frontier:
        cost, node = heapq.heappop(frontier)
        if cost > best_cost.get(node, float("inf")):
            continue
        nodes_expanded += 1
        if node == goal:
            return SearchResult(_reconstruct(came_from, start, goal), cost,
                                 nodes_expanded, time.perf_counter() - t0)

        for edge in graph.neighbours(node):
            new_cost = cost + edge.distance
            if new_cost < best_cost.get(edge.to, float("inf")):
                best_cost[edge.to] = new_cost
                came_from[edge.to] = node
                heapq.heappush(frontier, (new_cost, edge.to))

    return SearchResult(None, float("inf"), nodes_expanded, time.perf_counter() - t0)


def a_star_search(
    graph: CampusGraph,
    start: str,
    goal: str,
    heuristic: Callable[[CampusGraph, str, str], float],
    accessibility_required: bool = True,
) -> SearchResult:
    """Improved method: A* search with an optional wheelchair-accessibility constraint.

    When accessibility_required is True, edges flagged wheelchair_accessible = False
    are excluded from the search space entirely (a hard constraint), which reflects
    the real needs of the target user group rather than treating accessibility as a
    soft cost penalty.
    """
    t0 = time.perf_counter()
    counter = 0  # tie-breaker so tuples with equal priority never compare CampusGraph/str
    frontier: list = [(heuristic(graph, start, goal), counter, 0.0, start)]
    came_from: dict = {}
    best_cost = {start: 0.0}
    nodes_expanded = 0

    while frontier:
        _, _, cost, node = heapq.heappop(frontier)
        if cost > best_cost.get(node, float("inf")):
            continue
        nodes_expanded += 1
        if node == goal:
            return SearchResult(_reconstruct(came_from, start, goal), cost,
                                 nodes_expanded, time.perf_counter() - t0)

        for edge in graph.neighbours(node):
            if accessibility_required and not edge.wheelchair_accessible:
                continue  # constraint: inaccessible segments are not valid actions
            new_cost = cost + edge.distance
            if new_cost < best_cost.get(edge.to, float("inf")):
                best_cost[edge.to] = new_cost
                came_from[edge.to] = node
                counter += 1
                priority = new_cost + heuristic(graph, edge.to, goal)
                heapq.heappush(frontier, (priority, counter, new_cost, edge.to))

    return SearchResult(None, float("inf"), nodes_expanded, time.perf_counter() - t0)
