import os

import psycopg2
from fastapi import FastAPI, Depends
from psycopg2.extras import RealDictCursor


app = FastAPI()


def db_connection():
    conn = psycopg2.connect(
        dbname=os.getenv("DBNAME", "workshop_db"),
        user=os.getenv("PGUSER", "postgres"),
        host=os.getenv("PGHOST", "localhost"),
        port=os.getenv("PGPORT", "5432"),
        cursor_factory=RealDictCursor,
    )
    try:
        yield conn
    finally:
        conn.close()


@app.get("/authors")
def list_authors(conn=Depends(db_connection)):
    with conn.cursor() as cur:
        cur.execute("SELECT 1 as test")
        rows = cur.fetchall()
        return rows
