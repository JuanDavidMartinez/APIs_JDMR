from fastapi import FastAPI
import psycopg2
import os

app = FastAPI()

# URL de conexión desde variables de entorno
DATABASE_URL = os.getenv("DATABASE_URL")

# Conexión
conn = psycopg2.connect(DATABASE_URL)

@app.get("/")
def read_root():
    return {"message": "API conectada a PostgreSQL en Neon 3 🚀"}

@app.get("/users")
def get_users():
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM users;")  # asume que existe tabla users
    rows = cur.fetchall()
    cur.close()

    return {"users": rows}
