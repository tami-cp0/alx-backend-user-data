#!/usr/bin/env python3
"""
Module for BasicAUTH class
"""
from api.v1.auth.auth import Auth
from typing import TypeVar
from models.user import User
from models.base import DATA
import base64


class BasicAuth(Auth):
    """
    Basic authentication class.
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Extracts the base64 encoding from the authorization header
        """
        if (
            not authorization_header
            or not isinstance(authorization_header, str)
            or not authorization_header.startswith('Basic ')
           ):
            return None

        return authorization_header.split(' ')[1]

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """
        Returns the decoded value of a Base64 string in
        base64_authorization_header
        """
        if (
            not base64_authorization_header
            or not isinstance(base64_authorization_header, str)
           ):
            return None

        try:
            # Convert the Base64 string to bytes
            base64_bytes = base64_authorization_header.encode('utf-8')
            # Decode the Base64 bytes to original bytes
            decoded_bytes = base64.b64decode(base64_bytes)
            # Convert the original bytes back to a string
            decoded_string = decoded_bytes.decode('utf-8')

            return decoded_string
        except Exception:
            return None

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
    ) -> (str, str):
        """
        Returns the user email and password from the Base64 decoded value.
        """
        if (
            not decoded_base64_authorization_header
            or not isinstance(decoded_base64_authorization_header, str)
            or ":" not in decoded_base64_authorization_header
        ):
            return (None, None)

        email, password = decoded_base64_authorization_header.split(':')

        return (email, password)

    def user_object_from_credentials(
        self, user_email: str, user_pwd: str
    ) -> TypeVar('User'):
        """
        Returns the User instance based on his email and password.
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

    def current_user(self, request=None) -> TypeVar('User'):
        """
        retrieves the User instance for a request
        """
        auth_header = self.authorization_header(request)
        if auth_header:
            base64_credentials = self.extract_base64_authorization_header(auth_header)
            decoded_credentials = self.decode_base64_authorization_header(base64_credentials)
            email, password = self.extract_user_credentials(decoded_credentials)
            user = self.user_object_from_credentials(email, password)
            return user
        
        return None
            