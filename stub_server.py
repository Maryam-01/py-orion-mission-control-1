#!/usr/bin/env python3
"""
Stub server for the Orion 7 Mission Control API.

Infrastructure -- you do not need to read or modify this file.
Run it with:  python stub_server.py
Stop with:   Ctrl+C

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
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

# ---- Load data from files ------------------------------------------------

_data_dir = os.path.join(os.path.dirname(__file__), "data")

with open(os.path.join(_data_dir, "missions.json")) as _f:
    missions = json.load(_f)

with open(os.path.join(_data_dir, "spacecraft.json")) as _f:
    spacecraft = json.load(_f)

with open(os.path.join(_data_dir, "crew.json")) as _f:
    crew = json.load(_f)

next_mission_id = max(m["id"] for m in missions) + 1

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
