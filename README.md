# Gold Investment AI Assistant

A FastAPI-based backend application that allows users to:
- Ask questions about gold investment
- Purchase digital gold
- Store purchase data in a SQLite database

## Tech Stack
- Python
- FastAPI
- SQLite
- Pydantic
- Uvicorn

## Features
- Chat API for investment queries
- Buy Gold API to simulate gold purchases
- Database storage for transactions
- Swagger API documentation

## Run the Project

1. Install dependencies

pip install -r requirements.txt

2. Run the server

uvicorn main:app --reload

3. Open in browser

http://127.0.0.1:8000/docs
