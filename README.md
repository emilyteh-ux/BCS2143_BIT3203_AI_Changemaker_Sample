# Accessible Campus Route Planner

This repository is a **worked model example** for the BCS2143/BIT3203 Artificial
Intelligence individual assignment (AI Changemaker Agent for Social Impact), Study Intake
202607. It is built from the official assignment template and shows the standard of
content, testing and Git practice expected in a real submission. It is not a submission
itself — do not submit this repository as your own work.

## Student information

- Student name: [Example] Not a real student submission
- Student ID: N/A — teaching model answer
- Programme: BCS / BIT
- Course code: BCS2143 / BIT3203
- GitHub username: siewkienmah (repository owner / lecturer)

## Project title

Accessible Campus Route Planner for Wheelchair Users

## Competition-ready project description (150 words max)

Many campus wayfinding tools return the shortest route without checking whether it is
usable by a wheelchair user, forcing students with mobility constraints onto undocumented
detours or through inaccessible stairs. The Accessible Campus Route Planner is a small
intelligent agent that models the campus as a graph of locations and paths, each labelled
with distance and wheelchair-accessibility, and finds the shortest route that is guaranteed
to be accessible. It compares an uninformed baseline (Uniform Cost Search) against an
informed A* search using an admissible straight-line-distance heuristic, and enforces
accessibility as a hard constraint rather than a soft preference. Automated tests confirm
the planner avoids inaccessible paths, fails safely when no accessible route exists, and
expands fewer search nodes than the baseline. The prototype supports SDG 4, 10 and 11 by
removing a daily independence barrier for mobility-constrained campus users.

## Problem summary

See `docs/problem_statement.md` for the full problem statement, evidence and SDG alignment.
In short: wheelchair users need routes that are guaranteed accessible, not just short, and
this is rarely available on standard campus maps.

## AI method

Two methods are implemented and compared (see `src/search.py`):
- **Baseline:** Uniform Cost Search (uninformed), shortest path by distance only.
- **Improved / principal method:** A* search with an admissible Euclidean-distance
  heuristic and a hard wheelchair-accessibility constraint on which edges may be used.

## PEAS

See `docs/peas_and_formulation.md` for the full formulation.
- **Performance measure:** accessible path cost (metres), nodes expanded, execution time.
- **Environment:** simulated campus map (`data/campus_map.json`).
- **Actuators:** prints the recommended route to the console.
- **Sensors:** reads the map file and the user's requested start/goal/accessibility flag.

## Installation

```powershell
py -V:3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Running the prototype

```bash
python src/main.py --start main_gate --goal lecture_hall_b
python src/main.py --start admin_block --goal library --no-accessibility
```

Valid location ids are the keys under `nodes` in `data/campus_map.json` (e.g. `main_gate`,
`library`, `lecture_hall_a`, `lecture_hall_b`, `cafeteria`, `student_center`,
`sports_complex`, `accessible_parking`, `elevator_tower`, `admin_block`).

## Testing

```bash
pytest tests/ -v
```

Four test cases are provided (accessibility constraint enforcement, baseline-vs-improved
comparison, failure handling with no accessible path, and a full-map end-to-end run).
Results and metrics are recorded in `results/test_results.md`.

## Repository structure

- `src/` — Python source code (graph loading, heuristic, search algorithms, CLI)
- `tests/` — automated test cases (pytest)
- `data/` — simulated campus map data
- `results/` — sample outputs, metrics and testing evidence
- `docs/` — problem statement, PEAS/formulation and Responsible AI notes
- `presentation/` — slide and video placeholders (see notes in that folder)
- `DEVELOPMENT_LOG.md` — development decisions and milestones
- `AI_USE_DECLARATION.md` — compulsory AI-use declaration

## Known limitations

- The campus map is small and fully simulated; a real deployment would need verified
  facilities data and a process for keeping accessibility attributes current.
- The CLI is not itself accessible (e.g. no screen-reader-specific output); a real
  deployment should consider interface accessibility, not just route accessibility.
- Distances and travel times do not account for weather, temporary obstructions or
  elevator downtime.

## Submission

Final deadline: **6 August 2026, 5:00 pm**. Submit the private repository URL, final
commit SHA and repository ZIP through eQIU. The written report is submitted through
Turnitin. See `DEVELOPMENT_LOG.md` for how this example paced work across the milestone
checkpoints.
