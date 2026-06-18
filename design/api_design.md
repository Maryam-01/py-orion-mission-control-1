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
| GET    |/spacecrafts | Returns a list of all spacecrafts      |        |  200        |  400   
| GET    | /spacecrafts/1| Returns a single spacecrafts at id_1 |        |  200        |  400 / 404
| DELETE |/spacecrafts/3 | Deletes a spacecraft                 |        |  204        |  400 / 404
| POST   |/spacecrafts   | Creates a new spacecraft             | json   |  201        |  400
| PATCH  |/spacecrafts/1 | Assigns a crew member to a spacecraft| json   |  200        |  400 / 404

## Crew

| Method | Path       |        Description                | Request Body | Success Code| Error Codes |
|--------|------------|-----------------------------------|--------------|-------------|-------------|
| GET    |/crews      | Returns a list of all crews       |              |  200        |  400  / 404 
| GET    | /crews/1| Returns a single crews at id_1       |              |  200        |  400  / 404
| DELETE |/crews/3 | Deletes a crews                      |              |  204        |  400  / 404
| POST   |/crews   | Creates a crews                      | json         |  201        |  400  
| PATCH  |/crews/1 | Assigns a crew member to crew        | json         |  200        |  400  / 404
