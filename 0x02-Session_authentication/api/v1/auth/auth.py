#!/usr/bin/env python3
"""
Authentication module for the API
"""
from flask import request, jsonify
from typing import List, TypeVar
import fnmatch
import os


class Auth:
    """Authentication class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Method to check if a route requires auth
        """
        if path is None or excluded_paths is None or not excluded_paths:
            return True

        path = path.rstrip('/') + '/'
        excluded_paths = [p.rstrip('/') + '/' for p in excluded_paths]

        return path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """
        Method to get the authorization header
        """
        if request is not None:
            return request.headers.get('Authorization', None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Method to get the current user
        """
        return None

    def session_cookie(self, request=None):
        """
        Get the Session ID from a cookie in the request."""
        if request is None:
            return None

        session_name = os.getenv('SESSION_NAME', '_my_session_id')

        session_id = request.cookies.get(session_name)

        return session_id
