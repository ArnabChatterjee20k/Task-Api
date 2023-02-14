from flask import Flask
from dotenv import load_dotenv , dotenv_values
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_api():
    """A factory function to return the api build with configurations , models and routes"""

    # loading configs
    load_dotenv()
    config = dotenv_values()
    
    app = Flask(__name__)
    app.config.from_mapping(config)
    db.init_app(app)


    # initialiasing the routes
    from api.Routes.TaskHandler import task
    app.register_blueprint(task,url_prefix="/task")

    return app