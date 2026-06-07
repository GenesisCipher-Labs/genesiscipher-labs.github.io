# HomeSafe Privacy Policy

**Last updated: June 7, 2026**

HomeSafe is a personal navigation tool that helps you compare route options based on safety signals available from public map data. It is built privacy-first: your location, routes, saved places, contacts, and reports are processed and stored on your device, and GenesisCipher Labs does not operate servers that receive your data.

This policy covers the HomeSafe apps on both **iOS** and **Android**. The apps are functionally the same; where they differ is the mapping provider each platform uses, noted below.

## Data we collect

**Precise location.** When you grant location permission, HomeSafe reads your device's current location to suggest nearby starting points, plot routes, and match routes against safety signals like nearby hospitals, police stations, metro entrances, pharmacies, and 24-hour stores. While a trip is active and the app is in use, it also measures how far you have drifted from your route to suggest a safer re-route. Location is used only while you are using the app — HomeSafe does not request background-location access and does not track you when the app is closed. It is never transmitted to GenesisCipher Labs.

**Maps, routing, and search.** To draw maps, compute routes, and look up places, the relevant coordinates and search text are sent from your device to the mapping provider for your platform — never to GenesisCipher Labs:

- **On iOS,** this is handled by **Apple MapKit and Core Location**, under [Apple's Maps & Privacy policy](https://www.apple.com/legal/privacy/data/en/apple-maps/). HomeSafe does not log, store, or transmit your searches to its own servers.
- **On Android,** there is no key-free Apple equivalent, so HomeSafe uses free, public **OpenStreetMap** services. Coordinates are sent directly from your device to these third-party services to function: map tiles from OpenStreetMap, route directions from OSRM (`routing.openstreetmap.de`, which receives your start, destination, and route coordinates), nearby points of interest from Overpass (`overpass-api.de`, which receives the route's bounding-box area), and place search from Nominatim (`nominatim.openstreetmap.org`, which receives your search text and a location bias). These requests carry no account or user ID, are not linked to your identity, and are governed by the OpenStreetMap Foundation's policies.

**On-device data.** The following is stored solely on your device (iOS UserDefaults / Android private storage) and never leaves it: saved and recent places, emergency contacts you add, community safety reports you submit (which expire automatically after 90 days), your temporary active-trip snapshot, and in-app "Safety Bestie" conversations. Clearing or uninstalling the app removes all of it.

## Data we do not collect

- We do not run analytics, telemetry, or crash reporting services.
- We do not use advertising identifiers and do not track you across apps or websites.
- We do not operate user accounts. There is no sign-in.
- We do not maintain servers that receive your data.
- We do not sell, rent, or share personal data for advertising or marketing.

## Emergency / SOS features

HomeSafe is decision support, not an emergency service. It does not contact, relay, or forward your location to 112, 1091, 1098, 181, or any emergency line, and has no partnership with any emergency service. When you choose to use SOS, HomeSafe only opens your phone's dialer pre-filled with an emergency number (you decide whether to call) and opens the system share sheet with a location link (you decide who receives it). Your contacts' phone numbers leave your device only through actions you explicitly take in your own dialer or messaging app.

## Permissions

- **Location:** required for route planning, scoring, and off-route detection, used only while the app is in use. You can revoke it at any time in your device settings (iOS: Settings → Privacy & Security → Location Services). Without it, the app cannot calculate routes.
- **Internet / network state (Android):** required to load maps, routes, search, and points of interest from the public services above.

## Children

HomeSafe is not directed at children under 13 and we do not knowingly collect data from them.

## Changes to this policy

We will update the "Last updated" date above when this policy changes. Material changes will be reflected in a new app release.

## Contact

Questions about this policy:
GenesisCipher Labs — genesiscipherlabs@gmail.com
