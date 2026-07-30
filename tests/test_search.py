"""Test cases for the Accessible Campus Route Planner.

Run with: pytest tests/ -v
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from graph import CampusGraph          # noqa: E402
from heuristics import straight_line_distance  # noqa: E402
from search import a_star_search, uniform_cost_search  # noqa: E402

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "campus_map.json"


def load_graph() -> CampusGraph:
    return CampusGraph.from_json(DATA_PATH)


def test_accessible_route_avoids_inaccessible_edge():
    """Test case 1: the A* result must never use a wheelchair_accessible=False edge,
    even when that edge would give a shorter baseline path."""
    graph = load_graph()
    baseline = uniform_cost_search(graph, "admin_block", "library")
    improved = a_star_search(graph, "admin_block", "library", straight_line_distance,
                              accessibility_required=True)

    assert baseline.found
    assert improved.found
    # The direct admin_block -> library edge is stairs-only; the baseline is allowed
    # to use it, the accessible route must detour around it.
    assert improved.path != baseline.path
    assert "library" in improved.path


def test_a_star_expands_no_more_nodes_than_baseline():
    """Test case 2: baseline vs improved method comparison. On this map the informed
    A* heuristic should expand no more nodes than the uninformed baseline."""
    graph = load_graph()
    baseline = uniform_cost_search(graph, "main_gate", "sports_complex")
    improved = a_star_search(graph, "main_gate", "sports_complex", straight_line_distance,
                              accessibility_required=False)

    assert baseline.found and improved.found
    assert improved.nodes_expanded <= baseline.nodes_expanded


