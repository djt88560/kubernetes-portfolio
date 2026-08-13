from fastapi import FastAPI
import logging
import os
from Backend.qualifications import qualifications
from Backend.create_connection import create_connection, query_data, query_a_levels, query_gcses, query_university, query_certifications, query_awards
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

@app.get("/api/GCSEs")
def GCSEs():

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

    gcses = query_gcses(conn)

    conn.close() 
    return gcses

@app.get("/api/University")
def University():

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

    university = query_university(conn)

    conn.close() 
    return university


@app.get("/api/Certifications")
def Certifications():

    conn = create_connection(
        host="database-service",
        database="postgres",
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        port=5432
    )

    if not conn:
        return {"error": "Failed to connect"}

    certifications = query_certifications(conn)

    conn.close()
    return certifications

@app.get("/api/Awards")
def Awards():

    conn = create_connection(
        host="database-service",
        database="postgres",
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        port=5432
    )

    if not conn:
        return {"error": "Failed to connect"}

    awards = query_awards(conn)

    conn.close()
    return awards