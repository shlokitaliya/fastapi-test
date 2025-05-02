from fastapi import FastAPI , Path, HTTPException
from typing import Optional
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
# import sql


class item(BaseModel):
    name: str
    price: float
    description: Optional[str] = None
class updateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    description: Optional[str] = None

app = FastAPI()

DB_NAME = "form_data.db"

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],  # Adjust this to your frontend's URL
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, PUT, etc.)
    allow_headers=["*"],  # Allows all headers
)

@app.post("/create_item")
def create_item( item: item):

    save_data(item.name,item.description, item.price)

    return {"successful":"item added to the database!"}

@app.get("/submissions")
def get_all_submissions():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM submission")
    rows = cursor.fetchall()
    conn.close()

    return [
        {"id": row[0], "name": row[1], "description": row[2], "price": row[3]}
        for row in rows
    ]
def save_data(name: str, description: str, price: int):
    conn = sqlite3.connect("form_data.db")
    cursor = conn.cursor()

    cursor.execute("""
                   
                   INSERT INTO submission (name, description, price)
        VALUES (?, ?, ?)
                   
                   """,(name, description, price))
    conn.commit()
    conn.close()
# save_data("shlok","i am very good at programming",1299)













@app.get("/health")
def health_check():
    return {"status": "ok"}
