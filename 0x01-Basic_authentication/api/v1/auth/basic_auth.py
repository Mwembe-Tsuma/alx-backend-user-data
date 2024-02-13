#!/usr/bin/env python3
"""
Basic Authentication module for the API
"""
from api.v1.auth.auth import Auth
from models.user import User
import re
import base64
import binascii
from typing import Tuple, TypeVar


class BasicAuth(Auth):
    """Basic auth class"""
    def extract_base64_authorization_header(
            self,
            authorization_header: str) -> str:
        """
        Method to extract the Base64 part of the Authorization header
        """
        if authorization_header is None or not isinstance(
                authorization_header, str):
            return None

        if not authorization_header.startswith('Basic '):
            return None

        base64_part = authorization_header.split(' ')[1]

        return base64_part

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str) -> str:
        """Method to decode the Base64 Authorization header"""
        if type(base64_authorization_header) == str:
            try:
                decoded_value = base64.b64decode(
                    base64_authorization_header,
                    validate=True,
                )
                return decoded_value.decode('utf-8')
            except (binascii.Error, UnicodeDecodeError):
                return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str) -> (str, str):
        """
        Method to extract user email and password from the decoded Value
        """
        if decoded_base64_authorization_header is None or not isinstance(
                decoded_base64_authorization_header, str):
            return None, None

        if ':' not in decoded_base64_authorization_header:
            return None, None

        usr_email, usr_pwd = decoded_base64_authorization_header.split(':', 1)
        return usr_email, usr_pwd

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> User:
        """
        Method to get the User instance based on email and password
        """
        if type(user_email) == str and type(user_pwd) == str:
            try:
                users = User.search({'email': user_email})
            except Exception:
                return None
            if len(users) <= 0:
                return None
            if users[0].is_valid_password(user_pwd):
                return users[0]
        return None
