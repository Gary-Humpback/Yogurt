# -*- coding: utf-8 -*-
"""
=======================================
Filename: user_service
Description: service for blueprint user
=======================================
"""
from server.app.common.utils import exec_service


class User:
    def __init__(self):
        pass

    @exec_service
    def register(self, form):
        pass

    @exec_service
    def login(self, form):
        pass

    @exec_service
    def logout(self, form):
        pass

    @exec_service
    def read(self, form):
        pass

    @exec_service
    def update(self, form):
        pass


if __name__ == '__main__':
    pass
