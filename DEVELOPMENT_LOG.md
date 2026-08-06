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

## 30 July 2026 — Technical checkpoint

- Formal problem formulation: completed in `docs/peas_and_formulation.md` (state, actions,
  transition model, goal test, path cost, heuristic).
- Working baseline: implemented `uniform_cost_search` in `src/search.py` and confirmed it
  finds correct shortest paths on the sample map.
- Algorithm or heuristic decisions: implemented `a_star_search` with the straight-line
  heuristic in `heuristics.py`; confirmed admissibility reasoning (no path can be shorter
  than the straight-line distance on this map).
- Testing completed: `tests/test_search.py` — first two test cases written and passing
  (accessibility constraint enforcement; baseline-vs-improved node comparison).
- Problems found and corrections: initial A* implementation compared graph objects when
  heap priorities tied, causing a `TypeError`; fixed by adding a monotonically increasing
  tie-breaker counter to the heap entries.

## 4 August 2026 — Readiness checkpoint

- Three test cases and results: expanded to four test cases including failure handling
  (`test_no_accessible_path_reports_failure_cleanly`) and a full-map end-to-end check
  (`test_full_map_route_has_plausible_cost`); all passing. Metrics recorded in
  `results/test_results.md`.
- Responsible AI reflection: completed in `docs/responsible_ai.md`, covering fairness,
  privacy, safety, transparency, accessibility and sustainability.
- Limitations: documented in README — small simulated map, no interface accessibility,
  no handling of temporary obstructions.
- Slides and video status: slide outline drafted in `presentation/README.md`; video
  script drafted, recording scheduled before final submission.
- Remaining work: polish README installation/testing instructions; finalise AI-use
  declaration; tag final commit.

## 6 August 2026 — Final submission

- Final commit SHA: recorded at the tag `final-submission` in this repository's history.
- Final tag: `final-submission`.
- Summary of final changes: finalised README (added project title, 150-word description,
  full run/test instructions), completed `AI_USE_DECLARATION.md`, confirmed all four tests
  pass, confirmed `requirements.txt` is accurate, reviewed `.gitignore` to ensure no
  secrets or personal data were ever committed.
