# Test Results

## Automated test suite

Command: `pytest tests/ -v`

| Test case | Expected outcome | Actual outcome |
|---|---|---|
| `test_accessible_route_avoids_inaccessible_edge` | Accessible route differs from baseline and never uses a stairs-only edge | PASSED |
| `test_a_star_expands_no_more_nodes_than_baseline` | A* (informed) expands ≤ nodes than UCS (uninformed) on the same query | PASSED |
| `test_no_accessible_path_reports_failure_cleanly` | Planner returns `found = False`, no crash, no invalid route | PASSED |
| `test_full_map_route_has_plausible_cost` | Full-map query finds a route with a plausible cost (100–250 m) | PASSED |

All 4 tests passed (0.01s).

## Manual scenario runs and metrics

### Scenario 1 — Main Gate to Lecture Hall B (accessibility required)

| Method | Path cost | Nodes expanded | Time |
|---|---|---|---|
| Baseline (UCS, no filter) | 137.0 m | 9 | 0.024 ms |
| Improved (A*, accessible) | 140.0 m | 7 | 0.027 ms |

The accessible route is 3 m (2.2%) longer because it detours via Student Center to avoid
the stairs-only Admin Block–Library edge. A* also expanded fewer nodes than the uninformed
baseline thanks to the admissible heuristic.

### Scenario 2 — Admin Block to Library (accessibility off, sanity check)

Both methods return the same 55 m direct path when the accessibility constraint is disabled,
confirming the constraint — not a bug — is what causes the detour in Scenario 1.

### Scenario 3 — Main Gate to Sports Complex (accessibility required)

| Method | Path cost | Nodes expanded | Time |
|---|---|---|---|
| Baseline (UCS, no filter) | 160.0 m | 10 | 0.029 ms |
| Improved (A*, accessible) | 163.0 m | 6 | 0.033 ms |

## Limitations observed

- On this small map, the accessible detour cost is modest (2–5%); on a larger, sparser real
  campus graph the gap could be larger and would be worth reporting to facilities managers as
  a case for adding ramps.
- Execution times are sub-millisecond on this toy graph and are not meaningful for performance
  claims; they are recorded only to demonstrate the comparison methodology at scale.
