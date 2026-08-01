from fastapi import FastAPI
import logging
import os
from Backend.qualifications import qualifications
from Backend.create_connection import create_connection, query_data, query_a_levels
app = FastAPI()
POSTGRES_PASSWORD = os.getenv("db_password")
POSTGRES_USER = os.getenv("db_user")
POSTGRES_HOST = os.getenv("db_host")

logging.basicConfig(level=logging.INFO)

@app.get("/healthcheck")
def healthcheck():
    """Basic health check endpoint, to verify this service is online."""
    return {"health_check": "OK"} 

@app.get("/api/query")
def query():
    conn = create_connection(
        host="database-service",
        database="postgres",
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        port=5432
    )

    if not conn:
        return {"error": "Failed to connect"}

    rows = query_data(conn, "test", limit=5)

    conn.close()

    return rows


@app.get("/api/A-Levels")
def A_Levels():

    conn = create_connection(
        host="database-service",
        database="postgres",
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        port=5432
    )
    print(conn.get_dsn_parameters())

    if not conn:
        return {"error": "Failed to connect"}

    alevels = query_a_levels(conn)

    conn.close() 
    return alevels

