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

            for p in excluded_paths:
                if p[-1] != "*":
                    if path == p:
                        return False
                    if path[0:-1] == p:
                        return False
                else:
                    if p[0:-1] in path:
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
