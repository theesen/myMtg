from flask import Flask

from app.config import Config
from app.database import db


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_object(Config)
    else:
        app.config.from_mapping(test_config)

    with app.app_context():
        db.init_app(app)

    # Register Blueprints
    from app.authentication import auth
    app.register_blueprint(auth.bp)

    from app.collection import cardlist
    app.register_blueprint(cardlist.bp)

    app.add_url_rule('/', endpoint='index')

    return app
