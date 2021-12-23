# -*- coding: utf-8 -*-
import logging
from flask import Flask
from flask_cors import CORS

from server.app.controller.user import user_route
from server.app.configs.config import Config
from server.app.common.utils import run_scheduler

logging.basicConfig(level=logging.INFO, filename=f'{Config.server_root}/logs/record.log', filemode='a',
                    format='%(asctime)s | %(name)s | %(levelname)s | %(message)s')


class Application:
    def __init__(self):
        self.template_folder = f'{Config.server_root}/web/dist'
        self.static_folder = f'{Config.server_root}/web/static'
        self.blueprints = [user_route]

    def engine(self):
        app = Flask(__name__, template_folder=self.template_folder, static_folder=self.static_folder)
        # register blueprint
        for blueprint in self.blueprints:
            app.register_blueprint(blueprint)
        # add scheduler task
        app = run_scheduler(app)
        # fix cors
        CORS(app, supports_credentials=True)
        return app


if __name__ == '__main__':
    Application().engine().run(debug=True, host='localhost', prot=9980)
