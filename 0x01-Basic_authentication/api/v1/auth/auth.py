#!/usr/bin/env python3
"""
Authentication module for the API
"""
from flask import request
from typing import List, TypeVar
import fnmatch


class Auth:
    """Authentication class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Method to check if a route requires auth
        """
        if path is None:
            return True

        if excluded_paths is None or not excluded_paths:
            return True

        for excluded_path in excluded_paths:
            if fnmatch.fnmatch(path, excluded_path):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Method to get the authorization header
        """
        if request is not None:
            return request.headers.get('Authorization', None)
        return None

        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Method to get the current user
        """
        return None
