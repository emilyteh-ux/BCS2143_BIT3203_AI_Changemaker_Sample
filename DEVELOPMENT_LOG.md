# Development Log

Record substantive decisions, implementation progress, testing and debugging. Do not list
trivial file saves. This example shows the level of substance expected at each checkpoint —
note how work is spread across the assignment period rather than completed in one sitting.

## 24 July 2026 — Concept checkpoint

- Problem and target users: wheelchair users and other mobility-constrained students/staff
  needing guaranteed-accessible routes between campus buildings.
- Evidence and social value: campus accessibility audits commonly report undocumented
  stairs/kerbs on "shortest" routes; no accessible-route planner is published for students.
- Draft PEAS: performance = accessible path cost; environment = campus map graph;
  actuators = printed route; sensors = map file + user query. Drafted in `docs/problem_statement.md`.
- Proposed AI method: A* search with an accessibility constraint, compared against an
  uninformed baseline.
- Risks or questions: need to confirm the heuristic is admissible before relying on it;
  need to decide whether accessibility should be a hard constraint or a soft penalty —
  decided on hard constraint, since a "slightly shorter but inaccessible" route is not
  actually usable by the target user.

