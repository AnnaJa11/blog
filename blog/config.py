
class Config:
    DEBUG = False
    SECRET_KEY = 'very_secret_key'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'

class ProductionConfig(Config):
    SECRET_KEY = 'super_secret_key'
    # In real production, use a real database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///production_database.db'
    # Set your desired configuration options here
    # Add other configuration options as needed