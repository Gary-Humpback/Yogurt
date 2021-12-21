# -*- coding: utf-8 -*-
"""
=======================================
Filename: user
Description: blueprint for user part
=======================================
"""
from flask import Blueprint

user_route = Blueprint('user', __name__, url_prefix='/user')


@user_route.route('/setting')
def setting():
    return 'i am user setting'
