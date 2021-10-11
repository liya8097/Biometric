import os
from flask import Flask
from . import db
from . import register
def create_app():
    app =  app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    app.register_blueprint(register.bp)   
    db.init_app(app)

    return app
