from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
# import sys
# sys.path.append('../')

db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    app.secret_key = os.urandom(24)

    db.init_app(app)

    login_manager.init_app(app)
    login_manager.login_view = 'login'
    login_manager.session_protection = "strong"

    # Auth模块
    from apps.Auth.route import init_route
    init_route(app)

    # # 新闻模块
    # from app.news.api import init_api
    # init_api(app)

    from apps.app import init_app
    app = init_app(app)

    return app
