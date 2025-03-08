# -*- coding: utf-8 -*-
"""
Created on Sat Mar  8 18:41:19 2025

@author: User
"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Therapist Client Management System!"}
