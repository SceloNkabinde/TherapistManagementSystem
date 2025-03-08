# -*- coding: utf-8 -*-
"""
Created on Sat Mar  8 18:41:19 2025

@author: User
"""

from fastapi import FastAPI
from database import engine, Base

app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Therapist Client Management System!"}
