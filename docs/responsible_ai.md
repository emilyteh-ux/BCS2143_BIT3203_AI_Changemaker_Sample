
# Responsible AI

**Fairness and bias.** The system scores routes using infrastructure and environmental
attributes — lighting, CCTV coverage, pedestrian activity, and simulated crime-risk — rather
than demographic or identity-based profiling of users or neighbourhoods. A risk in a real
deployment is incomplete or outdated safety data (e.g. a streetlight that is broken but not
yet reported, or a CCTV camera that is offline); mitigation would be a user-reporting channel
and periodic data audits so no area is unfairly over- or under-penalised by the crime-risk
factor.

**Privacy.** The agent processes sensitive real-time data, including the user's live location,
destination, and, through Guardian Mode, an emergency contact. A real deployment should
discard location data once a journey ends, only share location with the emergency contact if
SOS is actually triggered, and avoid logging individual users' routes or journey history
without consent.

**Safety.** Incorrect or outdated lighting, CCTV, or crime-risk labels could route a user onto
a road that is less safe than the score suggests. Mitigation: recalculate routes when
conditions change (e.g. a road closure or construction), source safety attributes from
verified data where possible, and keep Guardian Mode and the SOS feature as a fallback if the
recommended route still leads to an unsafe situation.

**Security.** Because Guardian Mode shares live location and can contact a third party, the
SOS pathway is a high-value target if the system is compromised. A production version would
need to restrict location-sharing and SOS activation to explicit user opt-in per journey, and
encrypt any transmitted location data, especially if it later accepts user-submitted safety
reports that would need validation and moderation before being trusted.

**Transparency.** The agent displays a safety score breakdown for each recommended route and
explains why a recalculation occurred (e.g. road closure detected), so the user can see what
trade-off was made — distance versus safety — rather than receiving an unexplained single
answer.

**Accessibility.** Route suggestions should also account for users with mobility constraints,
such as avoiding stairs or poorly maintained pavements, alongside safety scoring. Offering
accessibility as an additional route filter, and eventually a screen-reader-friendly or voice
interface, would be a natural real-world extension beyond the current prototype.

**Environmental sustainability.** By making walking feel safer, SafeRoute AI supports walking
as a low-emission mode of urban transport. The underlying algorithms are also lightweight
(small graph, no training required), so computational and energy cost is negligible — a minor
positive rather than a significant sustainability finding on its own.

**Limitations.** This project is a prototype built on simulated safety data rather than a live
feed from city infrastructure, so its outputs should be read as a demonstration of the
approach rather than a validated safety tool. A real deployment would need agreements with
city authorities or facilities offices for genuine lighting, CCTV, and crime-risk data, along
with a clear process for keeping that data current as conditions on the ground change.
