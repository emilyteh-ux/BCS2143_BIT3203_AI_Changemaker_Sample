# Tests

Four test cases are provided in `test_search.py`, covering: accessibility-constrained routing,
a baseline-vs-improved-method comparison (nodes expanded), failure handling when no accessible
route exists, and an end-to-end run against the full sample map. Run with:

```
pytest tests/ -v
```

Sample console output and metrics are recorded in `results/test_results.md`.
