#!/usr/bin/env python3
"""
Basic Authentication module for the API
"""
from api.v1.auth.auth import Auth


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
