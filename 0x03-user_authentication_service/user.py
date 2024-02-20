#!/usr/bin/env python3
"""
Module to define the User model using SQLAlchemy mapping declaration.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """
    SQLAlchemy model for the users table.

    Attributes:
    - id: integer, primary key
    - email: non-nullable string
    - hashed_password: non-nullable string
    - session_id: nullable string
    - reset_token: nullable string
    """

    __tablename__ = 'users'

    id: int = Column(Integer, primary_key=True)
    email: str = Column(String(length=250), nullable=False)
    hashed_password: str = Column(String(length=250), nullable=False)
    session_id: str = Column(String(length=250), nullable=True)
    reset_token: str = Column(String(length=250), nullable=True)
