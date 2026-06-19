import psycopg2
import json


def seed():

    conn = psycopg2.connect(dbname="mission_control")
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS crews")
    cur.execute("DROP TABLE IF EXISTS missions")
    cur.execute("DROP TABLE IF EXISTS spacecrafts")



    cur.execute("""
        CREATE TABLE IF NOT EXISTS spacecrafts(
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                type VARCHAR(255) NOT NULL,
                fuel_capacity INT NOT NULL,
                payload_limit INT NOT NULL 
                );
                """)
        
    cur.execute("""
        CREATE TABLE IF NOT EXISTS missions(
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                destination VARCHAR(255) NOT NULL,
                status VARCHAR(50) NOT NULL,
                spacecraft_id INT REFERENCES spacecrafts(id)
                );
                """)
        
    cur.execute("""
        CREATE TABLE IF NOT EXISTS crews(
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                role VARCHAR(255) NOT NULL,
                clearance VARCHAR(50) NOT NULL,
                mission_id INT REFERENCES missions(id)
                );
                """)
        
        ## Seed the database




    with open("data/spacecraft.json") as f:
            spacecraft_data = json.load(f)

    for sc in spacecraft_data:
            cur.execute(
                "INSERT INTO spacecrafts (id, name, type, fuel_capacity, payload_limit) VALUES (%s, %s, %s, %s, %s)",
                (sc["id"], sc["name"], sc["type"], sc["fuel_capacity"], sc["payload_limit"])
                )

    with open("data/missions.json") as f:
            missions_data = json.load(f)

            for mission in missions_data:
                cur.execute(
                    "INSERT INTO missions (id, name, destination, status, spacecraft_id ) VALUES (%s, %s, %s, %s, %s)",
                    (mission["id"], mission["name"], mission["destination"], mission["status"], mission["spacecraft_id"])

                )

    with open("data/crew.json") as f:
            crew_data = json.load(f)

            for crew in crew_data:
            
                cur.execute(
                    "INSERT INTO crews (id, name, role, clearance, mission_id) VALUES (%s, %s, %s, %s, %s)",
                    (crew["id"], crew["name"], crew["role"], crew["clearance"], crew["mission_id"])

                    )



            conn.commit()
            cur.close()
            conn.close()
            

            print("Database created successfully")

if __name__ == "__main__":
    seed()
    

    


