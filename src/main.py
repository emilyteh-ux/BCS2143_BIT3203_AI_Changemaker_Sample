"""Command-line entry point for the Accessible Campus Route Planner.

Example
-------
python src/main.py --start main_gate --goal lecture_hall_b
python src/main.py --start main_gate --goal lecture_hall_b --no-accessibility
"""

from __future__ import annotations

import argparse
from pathlib import Path

from graph import CampusGraph
from heuristics import straight_line_distance
from search import a_star_search, uniform_cost_search

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "campus_map.json"


def describe_path(graph: CampusGraph, path: list[str]) -> str:
    return " -> ".join(graph.name(n) for n in path)


def main() -> None:
    parser = argparse.ArgumentParser(description="Accessible Campus Route Planner")
    parser.add_argument("--start", default="main_gate")
    parser.add_argument("--goal", default="lecture_hall_b")
    parser.add_argument("--no-accessibility", action="store_true",
                         help="disable the wheelchair-accessibility constraint")
    args = parser.parse_args()

    graph = CampusGraph.from_json(DATA_PATH)

    baseline = uniform_cost_search(graph, args.start, args.goal)
    improved = a_star_search(
        graph, args.start, args.goal, straight_line_distance,
        accessibility_required=not args.no_accessibility,
    )

    print(f"Route request: {graph.name(args.start)} -> {graph.name(args.goal)}")
    print(f"Accessibility required: {not args.no_accessibility}\n")

    print("Baseline (Uniform Cost Search, no accessibility filter)")
    if baseline.found:
        print(f"  Path: {describe_path(graph, baseline.path)}")
        print(f"  Cost: {baseline.cost:.1f} m | Nodes expanded: {baseline.nodes_expanded} "
              f"| Time: {baseline.execution_time_s * 1000:.3f} ms")
    else:
        print("  No path found.")

    print("\nImproved (A* with accessibility constraint)")
    if improved.found:
        print(f"  Path: {describe_path(graph, improved.path)}")
        print(f"  Cost: {improved.cost:.1f} m | Nodes expanded: {improved.nodes_expanded} "
              f"| Time: {improved.execution_time_s * 1000:.3f} ms")
    else:
        print("  No accessible path found between these locations.")


if __name__ == "__main__":
    main()
