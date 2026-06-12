# Mission Control API - First Draft

_Felix Ramos_

This is a sketch of what the Mission Control API should look like. I have listed the endpoints I think we need. Have a read through before we start building and let me know if anything looks off.

| Method | Path | Description |
|--------|------|-------------|
| GET | /getAllMissions | Returns a list of all missions |
| GET | /getMissionById?id=1 | Returns a single mission |
| GET | /deleteMission?id=3 | Deletes a mission |
| POST | /createMission | Creates a new mission |
| POST | /updateMission | Updates an existing mission |
| GET | /getSpacecraftList | Returns all spacecraft |
| GET | /getSpacecraftById?id=2 | Returns a single spacecraft |
| GET | /crew_members | Returns all crew members |
| GET | /getCrewByMission?mission_id=1 | Returns crew assigned to a mission |
| POST | /assignCrewToMission | Assigns a crew member to a mission |
