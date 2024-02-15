#!/usr/bin/env python3
"""
Route module for the API
"""

from api.v1.auth.auth import Auth
from typing import TypeVar
from models.user import User
import base64
from uuid import uuid4


class SessionAuth(Auth):
    """ Session Authentication Class """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Create a Session ID for a given user_id."""
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())

        self.user_id_by_session_id[session_id] = user_id

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Retrieve a User ID based on a Session ID."""
        if session_id is None or not isinstance(session_id, str):
            return None

        user_id = self.user_id_by_session_id.get(session_id)

        return user_id

    def current_user(self, request=None):
        """Return user instance based on cookie values."""
        if request is None:
            return None

        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)

        if user_id is None:
            return None

        user = User.get(user_id)
        return user

    def destroy_session(self, request=None):
        """
        Destroy a user session, logging them out."""
        if request is None:
            return False
        session_cookies = self.session_cookies(request)
        if session_cookies is None:
            return False
        user_id = self.user_id_for_session_id(session_cookies)
        if user_id is None:
            return False
        del self.user_id_by_session_id[session_cookies]
        return True
