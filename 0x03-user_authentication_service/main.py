#!/usr/bin/env python3
"""
Main file
"""
from auth import Auth
import requests


BASE_URL = "http://127.0.0.1:5000"


def register_user(email: str, password: str) -> None:
    """Register user"""
    response = requests.post(
        f"{BASE_URL}/users",
        data={"email": email, "password": password}
    )
    assert response.status_code == 201
    print("User registered successfully.")


def log_in_wrong_password(email: str, password: str) -> None:
    """Wrong password"""
    response = requests.post(
        f"{BASE_URL}/sessions",
        data={"email": email, "password": password}
    )
    assert response.status_code == 401
    print("Incorrect password handling successful.")


def log_in(email: str, password: str) -> str:
    """Logged in user"""
    response = requests.post(
        f"{BASE_URL}/sessions",
        data={"email": email, "password": password}
    )
    assert response.status_code == 200
    print("User logged in successfully.")
    return response.json()["session_id"]


def profile_unlogged() -> None:
    """Unlogged profile"""
    response = requests.get(f"{BASE_URL}/profile")
    assert response.status_code == 403
    print("Unlogged profile access handling successful.")


def profile_logged(session_id: str) -> None:
    """Logged profile"""
    headers = {"Cookie": f"session_id={session_id}"}
    response = requests.get(f"{BASE_URL}/profile", headers=headers)
    assert response.status_code == 200
    print("Logged profile access handling successful.")


def log_out(session_id: str) -> None:
    """Log out user"""
    headers = {"Cookie": f"session_id={session_id}"}
    response = requests.delete(f"{BASE_URL}/sessions", headers=headers)
    assert response.status_code == 200
    print("User logged out successfully.")


def reset_password_token(email: str) -> str:
    """ password reset"""
    response = requests.post(
        f"{BASE_URL}/reset_password",
        data={"email": email}
    )
    assert response.status_code == 200
    print("Reset password token generated successfully.")
    return response.json()["reset_token"]


def update_password(email: str, reset_token: str, new_password: str) -> None:
    response = requests.put(
        f"{BASE_URL}/reset_password",
        data={
            "email": email,
            "reset_token": reset_token,
            "new_password": new_password
            }
    )
    assert response.status_code == 200
    print("Password updated successfully.")


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":
    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
