# -*- coding: utf-8 -*-
from flask import Flask
from server.app.controller.user import user_route

app = Flask(__name__)
app.register_blueprint(user_route)


@app.route('/')
def index():
    return 'welcome to Yogurt'


if __name__ == '__main__':
    app.run(debug=True, host='localhost', prot=9980)
