import os
from flask import Flask, render_template
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from .config import config

db = SQLAlchemy()
csrf = CSRFProtect()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message = 'Please log in to access this page.'


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    csrf.init_app(app)
    login_manager.init_app(app)
    Migrate(app, db)

    # authパッケージのビューをインポートして、Blueprintを登録
    from .auth import views as auth_views
    app.register_blueprint(auth_views.auth, url_prefix='/auth')

    # uploaderパッケージのビューをインポートして、Blueprintを登録
    from .uploader import views as uploader_views
    app.register_blueprint(uploader_views.uploader, url_prefix='/uploader')

    # ルートページ
    @app.route('/')
    def index():
        return render_template('index.html')

    return app


# app = create_app()
