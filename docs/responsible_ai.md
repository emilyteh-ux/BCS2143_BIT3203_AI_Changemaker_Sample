# Responsible AI

**Fairness and bias.** The accessibility constraint is a hard exclusion rather than a soft
penalty, so the agent cannot silently trade away accessibility for a shorter route. A risk in
a real deployment is incomplete or outdated accessibility data (e.g. a ramp under repair);
mitigation would be a user-reporting channel and periodic data audits.

**Privacy.** The prototype does not collect, store or transmit any personal or location data
about individual users; it only reads a static, simulated map file and a one-off route request.
A real deployment should avoid logging individual users' routes without consent.

**Safety.** Incorrect accessibility labels could route a user into a physically inaccessible
or unsafe path. Mitigation: source accessibility attributes from verified facilities data,
and clearly flag when no accessible route exists rather than silently returning an
inaccessible one (implemented and tested — see `test_no_accessible_path_reports_failure_cleanly`).

**Security.** The map data file has no write access from user input in this prototype, which
avoids injection-style risks. A production version accepting user-submitted accessibility
reports would need input validation and moderation before trusting new data.

**Transparency.** The CLI prints both the baseline and the accessibility-constrained route so
a user or evaluator can see what trade-off was made (distance vs accessibility) rather than
receiving an unexplained single answer.

**Accessibility.** Accessibility is the core purpose of this project rather than an add-on;
the interface itself (a simple CLI) is a limitation for some users and a screen-reader-friendly
or voice interface would be a natural real-world extension.

**Environmental sustainability.** The algorithms are lightweight (small graph, no training),
so computational and energy cost is negligible; this is noted as a minor positive rather than
a significant sustainability finding.
