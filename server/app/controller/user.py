# -*- coding: utf-8 -*-
"""
=======================================
Filename: user
Description: blueprint for user part
=======================================
"""
from flask import Blueprint
from flask import request
from server.app.common.utils import read_request, process_response
from server.app.services.user_service import User

user_route = Blueprint('user', __name__, url_prefix='/user')
operator = User()


@user_route.route('/register', methods=('POST', ))
def register():
    req = read_request(request, 'userRegister')
    return process_response(operator.register(req))


@user_route.route('/login')
def login():
    req = read_request(request, 'userLogin')
    return process_response(operator.login(req))


@user_route.route('/logout')
def logout():
    req = read_request(request, 'userLogout')
    return process_response(operator.logout(req))


@user_route.route('/setting')
def read_settings():
    req = read_request(request, 'userReadSetting')
    return process_response(operator.read(req))


@user_route.route('/update_setting')
def update_settings():
    req = read_request(request, 'userUpdateSetting')
    return process_response(operator.update(req))
