from copy import deepcopy
from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Orion 7 Mission Control API (Stub)")

# ---------------------------------------------------------------------------
# Hardcoded seed data — this is a stub server. No database is involved.
# ---------------------------------------------------------------------------

_missions = [
    {"mission_id": 1, "name": "Artemis I", "destination": "Lunar Orbit", "status": "complete"},
    {"mission_id": 2, "name": "Phoenix", "destination": "Mars", "status": "active"},
    {"mission_id": 3, "name": "Horizon", "destination": "Deep Space", "status": "planned"},
    {"mission_id": 4, "name": "Atlas", "destination": "Mars", "status": "planned"},
    {"mission_id": 5, "name": "Meridian", "destination": "Lunar Surface", "status": "active"},
]

_spacecraft = [
    {"spacecraft_id": 1, "name": "Pegasus", "type": "crewed", "fuel_capacity": 45000, "mission_id": 2},
    {"spacecraft_id": 2, "name": "Voyager II", "type": "crewed", "fuel_capacity": 42000, "mission_id": 5},
    {"spacecraft_id": 3, "name": "Sentinel", "type": "uncrewed", "fuel_capacity": 28000, "mission_id": 1},
    {"spacecraft_id": 4, "name": "Nomad", "type": "uncrewed", "fuel_capacity": 31000, "mission_id": 3},
    {"spacecraft_id": 5, "name": "Argo", "type": "crewed", "fuel_capacity": 50000, "mission_id": 4},
    {"spacecraft_id": 6, "name": "Helios", "type": "uncrewed", "fuel_capacity": 22000, "mission_id": None},
    {"spacecraft_id": 7, "name": "Eclipse", "type": "crewed", "fuel_capacity": 47000, "mission_id": None},
    {"spacecraft_id": 8, "name": "Polaris", "type": "uncrewed", "fuel_capacity": 19000, "mission_id": None},
]

_crew = [
    {"crew_id": 1, "name": "Commander Yara Osei", "role": "Mission Commander", "clearance_level": 5, "mission_id": 2},
    {"crew_id": 2, "name": "Dr. Anika Sorensen", "role": "Flight Surgeon", "clearance_level": 4, "mission_id": 2},
    {"crew_id": 3, "name": "Felix Ramos", "role": "Systems Engineer", "clearance_level": 3, "mission_id": 2},
    {"crew_id": 4, "name": "Lt. Chen Wei", "role": "Pilot", "clearance_level": 4, "mission_id": 5},
    {"crew_id": 5, "name": "Dr. Priya Nair", "role": "Mission Specialist", "clearance_level": 3, "mission_id": 5},
    {"crew_id": 6, "name": "Sgt. Marcus Torres", "role": "Engineer", "clearance_level": 3, "mission_id": 5},
    {"crew_id": 7, "name": "Dr. Leila Farouk", "role": "Geologist", "clearance_level": 3, "mission_id": 4},
    {"crew_id": 8, "name": "Lt. Dmitri Volkov", "role": "Pilot", "clearance_level": 4, "mission_id": 4},
    {"crew_id": 9, "name": "Dr. Amara Diallo", "role": "Astrophysicist", "clearance_level": 4, "mission_id": 4},
    {"crew_id": 10, "name": "Eng. Sofia Eriksson", "role": "Engineer", "clearance_level": 2, "mission_id": None},
    {"crew_id": 11, "name": "Lt. James Okafor", "role": "Pilot", "clearance_level": 4, "mission_id": None},
    {"crew_id": 12, "name": "Dr. Hannah Kim", "role": "Mission Specialist", "clearance_level": 3, "mission_id": None},
]

_next_mission_id = 6


# ---------------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------------

class MissionCreate(BaseModel):
    name: str
    destination: str
    status: str = "planned"


# ---------------------------------------------------------------------------
# Missions
# ---------------------------------------------------------------------------

@app.get("/missions")
def get_missions(status: Optional[str] = None, destination: Optional[str] = None):
    results = deepcopy(_missions)
    if status is not None:
        results = [m for m in results if m["status"] == status]
    if destination is not None:
        results = [m for m in results if m["destination"] == destination]
    return results


@app.get("/missions/{mission_id}")
def get_mission(mission_id: int):
    for mission in _missions:
        if mission["mission_id"] == mission_id:
            return mission
    raise HTTPException(status_code=404, detail=f"No mission found with id {mission_id}")


@app.post("/missions", status_code=201)
def create_mission(body: MissionCreate):
    global _next_mission_id
    new_mission = {
        "mission_id": _next_mission_id,
        "name": body.name,
        "destination": body.destination,
        "status": body.status,
    }
    _missions.append(new_mission)
    _next_mission_id += 1
    return new_mission


# ---------------------------------------------------------------------------
# Spacecraft
# ---------------------------------------------------------------------------

@app.get("/spacecraft")
def get_spacecraft():
    return deepcopy(_spacecraft)


@app.get("/spacecraft/{spacecraft_id}")
def get_one_spacecraft(spacecraft_id: int):
    for sc in _spacecraft:
        if sc["spacecraft_id"] == spacecraft_id:
            return sc
    raise HTTPException(status_code=404, detail=f"No spacecraft found with id {spacecraft_id}")


# ---------------------------------------------------------------------------
# Crew
# ---------------------------------------------------------------------------

@app.get("/crew")
def get_crew():
    return deepcopy(_crew)


@app.get("/crew/{crew_id}")
def get_crew_member(crew_id: int):
    for member in _crew:
        if member["crew_id"] == crew_id:
            return member
    raise HTTPException(status_code=404, detail=f"No crew member found with id {crew_id}")
