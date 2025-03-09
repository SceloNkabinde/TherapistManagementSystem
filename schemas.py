# -*- coding: utf-8 -*-
"""
Created on Sat Mar  8 21:20:16 2025

@author: User
"""

from pydantic import BaseModel
from typing import Optional

class ClientCreate(BaseModel):
    name: str
    email: str
    phone: Optional[str] = None

class ClientUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None

class Client(BaseModel):
    id: int
    name: str
    email: str
    phone: Optional[str] = None

    class Config:
        orm_mode = True
