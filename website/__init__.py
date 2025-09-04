from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
import os

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()

DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['APP_NAME'] = 'TIGO'

    # App config
    app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY", "helloworld")

    # DATABASE_URL is set by Render for PostgreSQL
    database_url = os.environ.get("DATABASE_URL")
    if database_url:
        # Make sure SQLAlchemy knows it's PostgreSQL
        if database_url.startswith("postgres://"):
            database_url = database_url.replace("postgres://", "postgresql://", 1)
        app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    else:
        # Fallback to local SQLite for dev
        app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}"

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions with app
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    # Import models so Flask-Migrate can detect them
    from .models import User, Post, Comment, Like, Category, Tag

    # Setup Login Manager
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
