#!/usr/bin/env python3
"""
Stub server for the Orion 7 Mission Control API.

Runs on http://localhost:8000
Stop with Ctrl+C.

Endpoints:
  GET    /missions          List all missions
  GET    /missions/{id}     Get a single mission
  POST   /missions          Create a mission
  DELETE /missions/{id}     Delete a mission
  GET    /spacecraft        List all spacecraft
  GET    /spacecraft/{id}   Get a single spacecraft
  GET    /crew              List all crew members
  GET    /crew/{id}         Get a single crew member
"""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer

# ---- Data ----------------------------------------------------------------

missions = [
    {
        "id": 1,
        "name": "Helios-1",
        "destination": "Mars",
        "status": "active",
        "spacecraft_id": 2,
    },
    {
        "id": 2,
        "name": "Helios-2",
        "destination": "Mars",
        "status": "planned",
        "spacecraft_id": None,
    },
    {
        "id": 3,
        "name": "Vega-1",
        "destination": "Venus",
        "status": "complete",
        "spacecraft_id": 1,
    },
    {
        "id": 4,
        "name": "Eos-1",
        "destination": "Europa",
        "status": "planned",
        "spacecraft_id": 3,
    },
]

spacecraft = [
    {
        "id": 1,
        "name": "Argo",
        "type": "crewed",
        "fuel_capacity": 12000,
        "payload_limit": 4500,
    },
    {
        "id": 2,
        "name": "Hermes",
        "type": "crewed",
        "fuel_capacity": 15000,
        "payload_limit": 6000,
    },
    {
        "id": 3,
        "name": "Pathfinder",
        "type": "uncrewed",
        "fuel_capacity": 8000,
        "payload_limit": 2000,
    },
    {
        "id": 4,
        "name": "Sentinel",
        "type": "uncrewed",
        "fuel_capacity": 6000,
        "payload_limit": 1500,
    },
]

crew = [
    {
        "id": 1,
        "name": "Dr. Amara Osei",
        "role": "Mission Specialist",
        "clearance": "level_4",
        "mission_id": 1,
    },
    {
        "id": 2,
        "name": "Commander Lena Vasquez",
        "role": "Pilot",
        "clearance": "level_5",
        "mission_id": 1,
    },
    {
        "id": 3,
        "name": "Dr. Kai Nakamura",
        "role": "Flight Surgeon",
        "clearance": "level_3",
        "mission_id": 1,
    },
    {
        "id": 4,
        "name": "Dr. Sara Okonkwo",
        "role": "Engineer",
        "clearance": "level_4",
        "mission_id": 3,
    },
    {
        "id": 5,
        "name": "Felix Ramos",
        "role": "Mission Specialist",
        "clearance": "level_4",
        "mission_id": None,
    },
    {
        "id": 6,
        "name": "Dr. Priya Singh",
        "role": "Data Scientist",
        "clearance": "level_3",
        "mission_id": 4,
    },
]

next_mission_id = 5

# ---- Handler -------------------------------------------------------------


class Handler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        print(f"  {self.command} {self.path}  -->  {args[1]}")

    def send_json(self, status, data):
        body = json.dumps(data, indent=2).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(body)

    def read_body(self):
        length = int(self.headers.get("Content-Length", 0))
        if length == 0:
            return {}
        return json.loads(self.rfile.read(length))

    def do_GET(self):
        path = self.path.rstrip("/")
        parts = path.strip("/").split("/")

        if parts[0] == "missions":
            if len(parts) == 1:
                self.send_json(200, {"missions": missions})
            elif len(parts) == 2 and parts[1].isdigit():
                mission = next(
                    (m for m in missions if m["id"] == int(parts[1])), None
                )
                if mission:
                    self.send_json(200, {"mission": mission})
                else:
                    self.send_json(404, {"error": "Mission not found"})
            else:
                self.send_json(404, {"error": "Not found"})

        elif parts[0] == "spacecraft":
            if len(parts) == 1:
                self.send_json(200, {"spacecraft": spacecraft})
            elif len(parts) == 2 and parts[1].isdigit():
                ship = next(
                    (s for s in spacecraft if s["id"] == int(parts[1])), None
                )
                if ship:
                    self.send_json(200, {"spacecraft": ship})
                else:
                    self.send_json(404, {"error": "Spacecraft not found"})
            else:
                self.send_json(404, {"error": "Not found"})

        elif parts[0] == "crew":
            if len(parts) == 1:
                self.send_json(200, {"crew": crew})
            elif len(parts) == 2 and parts[1].isdigit():
                member = next(
                    (c for c in crew if c["id"] == int(parts[1])), None
                )
                if member:
                    self.send_json(200, {"crew_member": member})
                else:
                    self.send_json(404, {"error": "Crew member not found"})
            else:
                self.send_json(404, {"error": "Not found"})

        else:
            self.send_json(404, {"error": "Not found"})

    def do_POST(self):
        global next_mission_id
        path = self.path.rstrip("/")

        if path == "/missions":
            body = self.read_body()
            if "name" not in body or "destination" not in body:
                self.send_json(
                    400, {"error": "name and destination are required"}
                )
                return
            new_mission = {
                "id": next_mission_id,
                "name": body["name"],
                "destination": body["destination"],
                "status": "planned",
                "spacecraft_id": body.get("spacecraft_id"),
            }
            missions.append(new_mission)
            next_mission_id += 1
            self.send_json(201, {"mission": new_mission})
        else:
            self.send_json(404, {"error": "Not found"})

    def do_DELETE(self):
        parts = self.path.rstrip("/").strip("/").split("/")

        if (
            len(parts) == 2
            and parts[0] == "missions"
            and parts[1].isdigit()
        ):
            mission_id = int(parts[1])
            mission = next(
                (m for m in missions if m["id"] == mission_id), None
            )
            if mission:
                missions.remove(mission)
                self.send_response(204)
                self.end_headers()
            else:
                self.send_json(404, {"error": "Mission not found"})
        else:
            self.send_json(404, {"error": "Not found"})


# ---- Entry point ---------------------------------------------------------

if __name__ == "__main__":
    server = HTTPServer(("localhost", 8000), Handler)
    print("Stub server running on http://localhost:8000")
    print("Ctrl+C to stop.")
    print()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
