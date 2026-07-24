# PEAS and Formal AI Problem Formulation

## PEAS

- **Performance measure:** total accessible walking distance (metres) of the returned route;
  secondary measures are nodes expanded and execution time, used to compare search methods.
- **Environment:** a static, simulated campus map of named locations connected by paths, each
  path labelled with distance, surface type and wheelchair accessibility. Partially observable
  only in the sense that a user may not know which paths are accessible in advance — the agent
  makes this observable by encoding it in the map.
- **Actuators:** outputs an ordered list of locations (the route) and reports it to the user via
  the command-line interface.
- **Sensors:** reads the campus map data file (`data/campus_map.json`) and the user's requested
  start location, goal location and accessibility requirement.

## State or variables

A state is the current location (node id) during search, paired with the accumulated path cost
and the path taken so far.

## Initial state

The user-specified start location (e.g. `main_gate`).

## Actions or domains

From any location, the available actions are "move to an adjacent connected location" via one
of that location's edges. When the accessibility constraint is active, only edges with
`wheelchair_accessible = true` are valid actions.

## Transition model or constraints

Moving along an edge transitions the agent from one node to the connected node and adds that
edge's distance to the accumulated path cost. The hard constraint is: if accessibility is
required, edges flagged `wheelchair_accessible = false` are excluded from the action set
entirely (not merely penalised).

## Goal test

The current location equals the user-specified goal location.

## Path cost

The sum of the `distance` values (metres) of every edge traversed from the start to the current
node.

## Heuristic, where applicable

`straight_line_distance` (Euclidean distance between the current node's coordinates and the
goal's coordinates) is used by A*. It is admissible because no walking path between two points
on this map can be shorter than the straight-line distance between them, so the heuristic never
overestimates the true remaining cost.
