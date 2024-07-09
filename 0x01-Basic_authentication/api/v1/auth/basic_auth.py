#!/usr/bin/env python3
"""
Module for BasicAUTH class
"""
from api.v1.auth.auth import Auth
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
    
    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str) -> str:
        """
        Returns the decoded value of a Base64 string in base64_authorization_header
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
