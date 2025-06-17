import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Application base configuration."""
    DEBUG = True
    SECRET_KEY = 'super-secret-key'
    #SQLite  databse URL
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "..", "taskup.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
