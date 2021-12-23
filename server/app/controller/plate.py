# -*- coding: utf-8 -*-
"""
=======================================
Filename: plate
Description: blueprint for plate part
=======================================
"""
from flask import Blueprint

user_route = Blueprint('plate', __name__, url_prefix='/plate')


@user_route.route('/resources')
def get_resources():
    return 'get resources'


@user_route.route('/view')
def view_plate():
    return 'view plate'


@user_route.route('/replay')
def replay():
    return 'replay'


@user_route.route('/delete_plate')
def delete_plate():
    return 'delete plate'


@user_route.route('/delete_replay')
def delete_replay():
    return 'delete replay'
