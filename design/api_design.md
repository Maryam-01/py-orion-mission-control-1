# API Design: Orion 7 Mission Control

## Missions

| Method | Path       |        Description                | Request Body | Success Code| Error Codes |
|--------|------------|-----------------------------------|--------------|-------------|-------------|
| GET    |  /missions | Returns a list of all missions    |              |  200        |  400   
| GET    | /missions/1| Returns a single mission at id_1  |              |  200        |  400 / 404
| DELETE |/missions/3 | Deletes a mission                 |              |  204        |  400 / 404
| POST   |/missions   | Creates a new mission             | json         |  201        |  400
| PATCH  |/missions/1 | Assigns a crew member to a mission| json         |  200        |  400 /404


## Spacecraft

| Method | Path       |        Description                | Request Body | Success Code| Error Codes |
|--------|------------|-----------------------------------|--------------|-------------|-------------|
| GET    |/spacecrafts | Returns a list of all spacecrafts |        |  200        |  400   
| GET    | /spacecrafts/{id}| Returns a single spacecrafts at id_1 |        |  200        |  400 / 404
| DELETE |/spacecrafts/{id} | Deletes a spacecraft                 |        |  204        |  400 / 404
| POST   |/spacecrafts   | Creates a new spacecraft        | json   |  201        |  400
| PATCH  |/spacecrafts/{id} | Assigns a crew member to a spacecraft| json   |  200        |  400 / 404

## Crew

| Method | Path       |        Description                | Request Body | Success Code| Error Codes |
|--------|------------|-----------------------------------|--------------|-------------|-------------|
| GET    |/crews      | Returns a list of all crews       |              |  200        |  400  / 404 
| GET    | /crews/{id}| Returns a single crews at id_1    |              |  200        |  400  / 404
| DELETE |/crews/{id} | Deletes a crews                   |              |  204        |  400  / 404
| POST   |/crews   | Creates a crews                      | json         |  201        |  400  
| PATCH  |/crews/{id} | Assigns a crew member to crew     | json         |  200        |  400  / 404


post endpoints - method, path, body 

 {
    "id": 1, int
    "name": "Dr. Amara Osei", str
    "role": "Mission Specialist", str
    "clearance": "level_4", str
    "mission_id": 1 int
  }

  patch endpoint - string , string, string, integer expect for it to update 