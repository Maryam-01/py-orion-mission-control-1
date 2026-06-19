import psycopg2
from fastapi import FastAPI
from fastapi import FastAPI, HTTPException

app = FastAPI()

def get_connection():
    return psycopg2.connect(dbname="mission_control")


@app.get("/missions")
def get_missions():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM missions")
    columns = [desc[0] for desc in cur.description]
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [dict(zip(columns, row)) for row in rows]




@app.get("/missions/{mission_id}")
def get_mission(mission_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM missions WHERE id = %s", (mission_id,))
    columns = [desc[0] for desc in cur.description]
    row = cur.fetchone()
    cur.close()
    conn.close()
    if row is None:
        raise HTTPException(status_code=404, detail="Mission not found")
    return dict(zip(columns, row))


@app.get("/crews")
def get_crews():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM crews")
    columns = [desc[0] for desc in cur.description]
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [dict(zip(columns, row)) for row in rows]



@app.get("/crews/{id}")
def get_crew(id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM crews WHERE id = %s", (id,))
    columns = [desc[0] for desc in cur.description]
    row = cur.fetchone()
    cur.close()
    conn.close()
    if row is None:
        raise HTTPException(status_code=404, detail="Crew not found")
    return dict(zip(columns, row))


@app.get("/spacecrafts")
def get_spacecraft():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM spacecrafts")
    columns = [desc[0] for desc in cur.description]
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [dict(zip(columns, row)) for row in rows]



@app.get("/spacecrafts/{id}")
def get_spacecraft(id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM spacecrafts WHERE id = %s", (id,))
    columns = [desc[0] for desc in cur.description]
    row = cur.fetchone()
    cur.close()
    conn.close()
    if row is None:
        raise HTTPException(status_code=404, detail="Spacecrafts not found")
    return dict(zip(columns, row))






@app.post("/missions")
def post_missions():
    conn = get_connection()
    cur = conn.cursor()
    names = cur.execute("INSERT INTO missions (id, name, destination, status, spacecraft_id ) VALUES (%s, %s, %s, %s, %s)",
                    (mission["id"], mission["name"], mission["destination"], mission["status"], mission["spacecraft_id"])

                )

    crews = []
    for name, crew_id in names:
        crews.append({
            "id": crew_id,
            "name": names
        })
    crews = cur.fetchall()
    cur.close()
    conn.close()
    return crews






@app.get("/crews/{id}")
def get_crew_member(id: int):
    conn = get_connection()
    cur = conn.cursor()

    # ✅ ONLY select the columns you want
    cur.execute("SELECT id, name FROM crews WHERE id = ?", (id,))
    row = cur.fetchone()

    cur.close()
    conn.close()

    if row is None:
        return {"error": "Crew not found"}

    return {
        "crew_id": row[0],
        "name": row[1]
    }