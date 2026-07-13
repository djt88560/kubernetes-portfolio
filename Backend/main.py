from fastapi import FastAPI
import logging
import os
from Backend.qualifications import qualifications
from Backend.create_connection import create_connection, query_data
app = FastAPI()
POSTGRES_PASSWORD = os.getenv("db_password")
POSTGRES_USER = os.getenv("db_user")
POSTGRES_HOST = os.getenv("db_host")

logging.basicConfig(level=logging.INFO)

@app.get("/healthcheck")
def healthcheck():
    """Basic health check endpoint, to verify this service is online."""
    return {"health_check": "OK"} 

@app.get("/query")
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


@app.get("/qualifications")
def statement():
    logging.info({
        "event": "GET method: qualifications called",
        "endpoint": "/qualifications"
    })
    try:
        return qualifications()
    except Exception as e:
        logging.error("API - 'statement', request failed")
        raise e

