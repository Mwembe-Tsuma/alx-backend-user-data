#!/usr/bin/env python3
"""
Encrypt Passwords using bcrypt

Usage:
    hashed_password = hash_password(password)
"""


import bcrypt


def hash_password(password: str) -> bytes:
    """Hashes a password using bcrypt with salt."""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Validates a password using bcrypt."""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
