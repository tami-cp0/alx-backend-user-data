#!/usr/bin/env python3
"""
Module for AUTH class
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Authentication class.
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Check which routes don't need authentication
        """
        if path and excluded_paths:
            if path[-1] != '/':
                path += '/'

            if path in excluded_paths:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Checks if Authorization header is present.
        """
        if request:
            auth = request.headers.get("Authorization", None)
            if auth:
                return auth

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Will be fully implemented later
        """
        return None
