
# PEAS and Formal AI Problem Formulation

## PEAS

**Performance measure (how success is judged):** The system is considered successful if it recommends the safest walking route while maintaining a reasonable travel time. Performance will be evaluated using route safety score, travel time, successful route completion, user preference satisfaction, and route recalculation efficiency when conditions change.

**Environment (where the agent operates):** The intelligent agent operates on a simulated map of a campus or city. It uses information about road distance, lighting, CCTV, pedestrian traffic, construction, and crime risk to find the safest route.

**Actuators (how the agent acts):** The agent recommends the safest walking route, displays route safety scores, provides safety warnings, recalculates routes when conditions change, activates Guardian Mode during the journey, and triggers the SOS feature when necessary.

**Sensors (what the agent perceives):** The agent receives the user's current location, destination, safety preferences, estimated travel time, and environmental information such as lighting conditions, CCTV availability, pedestrian activity, road closures, and simulated crime-risk data.

## Environment properties

- **Observable: Partially** — the agent has a full digital map of roads and their attributes, but it cannot directly perceive every real-world condition at the moment of travel (e.g. a streetlight that has just failed, or a crowd that has just dispersed); it relies on the most recent data available.
- **Deterministic: No** — taking the same action (walking a given road) does not always lead to the same outcome, since real-world safety conditions such as pedestrian activity or crime risk can vary between journeys even on an identical route.
- **Episodic or sequential: Sequential** — each decision (which road to take next) affects future decisions, since the agent's remaining options depend on the intersection it currently occupies.
- **Static or dynamic: Dynamic** — the environment can change while the agent is deliberating or the user is travelling, such as a new road closure or a construction zone appearing mid-journey.
- **Discrete or continuous: Discrete** — the map is represented as a finite set of intersections (nodes) and road segments (edges), rather than continuous coordinates, so the state and action spaces are both countable.

## State or variables

The state consists of the user's current location, destination, and the safety information of each road segment. Each road contains attributes such as walking distance, lighting conditions, CCTV availability, pedestrian activity, construction status, and crime-risk level. The user's safety preference (e.g., prioritising safety over speed) is also considered during route evaluation.

## Initial state

The initial state is the user's current location when they start their journey. The destination and preferred safety settings are entered before the AI begins searching for the safest route.

## Actions or domains

The available actions are moving from one intersection to another through connected roads on the map. At each intersection, the AI evaluates all possible paths and selects the next road based on its heuristic evaluation.

## Transition model or constraints

When the AI selects a road, the user's current location changes to the next connected intersection. The AI continuously updates the route if changes occur, such as road closures, construction, or if the user deviates from the recommended path.

## Goal test

The goal is achieved when the user successfully reaches the destination using a route that satisfies the selected safety preferences while maintaining a reasonable travel time.

## Path cost

The path cost is calculated using multiple factors instead of distance alone. Roads with poor lighting, low pedestrian activity, higher crime-risk levels, construction zones, or no CCTV coverage receive higher costs, while safer roads receive lower costs. This encourages the AI to select routes that maximise safety rather than simply minimising distance.

## Heuristic, where applicable

The heuristic estimates the safest remaining route to the destination by considering both the remaining walking distance and safety factors. The AI assigns higher priority to routes with better lighting, CCTV coverage, and higher pedestrian activity, while penalising routes with higher crime-risk levels or unsafe conditions. This enables the A* algorithm to efficiently search for the safest practical route.

## Testing strategy

The formulation will be evaluated across at least three distinct map scenarios of varying density and layout, each comparing a baseline shortest-path route (safety weight of zero) against a safety-optimised route. For each scenario, three measures are recorded: the additional walking distance introduced by prioritising safety, the resulting reduction in overall route risk score, and the number of nodes expanded during the search, as an indicator of computational efficiency. This allows the trade-off between distance, safety, and search cost to be assessed directly, rather than assumed.

## Appendix: draft simple reflex agent rules (early sketch, Part D)

**Rule 1**
If: The selected route contains a road segment with a high crime-risk level or poor lighting.
Then: Recommend an alternative route with a higher safety score.

**Rule 2**
If: The user deviates from the recommended safe route.
Then: Recalculate and recommend the safest route from the user's current location.

**Rule 3**
If: The user does not reach the destination within the expected travel time and does not respond to the Guardian Mode safety check.
Then: Activate the SOS feature and notify the user's emergency contact with the user's last known location.
