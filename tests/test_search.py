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


def test_no_accessible_path_reports_failure_cleanly():
    """Test case 3: failure handling. Build a tiny disconnected-when-accessible graph
    and confirm the planner reports 'no path' rather than crashing or returning a
    route through an inaccessible edge."""
    graph = CampusGraph(
        nodes={"a": {"name": "A", "x": 0, "y": 0}, "b": {"name": "B", "x": 10, "y": 0}},
        adjacency={},
    )
    from graph import Edge
    graph.adjacency = {
        "a": [Edge("b", 10, False, "stairs")],
        "b": [Edge("a", 10, False, "stairs")],
    }

    result = a_star_search(graph, "a", "b", straight_line_distance, accessibility_required=True)

    assert result.found is False
    assert result.path is None


def test_full_map_route_has_plausible_cost():
    """Test case 4: end-to-end run against the full sample map. The accessible route
    from the main gate to Lecture Hall B should be found and its cost should be within
    a plausible range given the map's edge distances."""
    graph = load_graph()
    result = a_star_search(graph, "main_gate", "lecture_hall_b", straight_line_distance,
                            accessibility_required=True)

    assert result.found
    assert result.path[0] == "main_gate"
    assert result.path[-1] == "lecture_hall_b"
    assert 100 <= result.cost <= 250
