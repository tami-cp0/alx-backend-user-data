#!/usr/bin/env python3
"""
Module for BasicAUTH class
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    Basic authentication class.
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        if (
            not authorization_header
            or not isinstance(authorization_header, str)
            or not authorization_header.startswith('Basic ')
           ):
            return None

        return authorization_header.split(' ')[1]
