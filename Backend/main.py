from fastapi import FastAPI
import logging
from Backend.qualifications import qualifications
app = FastAPI()

logging.basicConfig(level=logging.INFO)

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

