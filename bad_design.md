# Mission Control API - First Draft

_Felix Ramos_

This is a sketch of what the Mission Control API should look like. I have listed the endpoints I think we need. Have a read through before we start building and let me know if anything looks off.

| Method | Path | Description |
|--------|------|-------------|
| GET | /getAllMissions | Returns a list of all missions | VERB
| GET | /getMissionsById?id=1 | Returns a single mission | VERB, enter missions (plural) first and then ID
| GET | /deleteMission?id=3 | Deletes a mission | WRONG METHOD, SHOULD BE DELETE
| POST | /createMission | Creates a new mission | VERB
| POST | /updateMission | Updates an existing mission | WRONG METHOD, SHOULD BE PATCH
| GET | /getSpacecraftList | Returns all spacecraft | VERB
| GET | /getSpacecraftById?id=2 | Returns a single spacecraft | VERB
| GET | /crew_members | Returns all crew members | FINE
| GET | /getCrewByMission?mission_id=1 | Returns crew assigned to a mission | VERB
| POST | /assignCrewToMission | Assigns a crew member to a mission | VERB
