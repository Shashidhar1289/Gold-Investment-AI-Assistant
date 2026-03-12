from fastapi import FastAPI
from chat_api import router as chat_router
from purchase_api import router as purchase_router
from database import create_table
import sqlite3

app = FastAPI(title="Gold Investment AI Assistant")

create_table()

app.include_router(chat_router)
app.include_router(purchase_router)


@app.get("/")
def home():
    return {"message": "Gold Investment AI Assistant Running"}

@app.get("/purchases")
def get_purchases():

    conn = sqlite3.connect("gold.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM purchases")

    rows = cursor.fetchall()

    conn.close()

    return rows