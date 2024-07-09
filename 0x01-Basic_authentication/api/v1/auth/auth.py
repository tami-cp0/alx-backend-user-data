#!/usr/bin/env python3
"""
Module for AUTH class
"""
from typing import List, TypeVar


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Will be fully implemented later
        """
        # if not (path or excluded_paths):
        #     return True

        # if path[-1] != '/':
        #     path += '/'

        # if path in excluded_paths:
        #     return False

        # return True
        return False

    def authorization_header(self, request=None) -> str:
        """
        Will be fully implemented later
        """
        # if not request:
        #     return None

        # auth = request.headers.get("Authorization", None)
        # if not auth:
        #     return None

        # return auth
        return False

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Will be fully implemented later
        """
        return None
