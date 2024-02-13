#!/usr/bin/env python3
"""
Authentication module for the API
"""
from flask import request
from typing import List, TypeVar


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
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Method to get the current user
        """
        return None
