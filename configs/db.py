from os import environ

print(environ.get("DB_HOST", "localhost"))

DATABASE = 'mysql'
USER = environ.get('DB_USERNAME')
PASSWORD = environ.get('DB_PASSWORD')
HOST = environ.get('DB_HOST')
PORT = '3306'
DB_NAME = environ.get('DB_DATABASE')

DATABASE_URL = '{}://{}:{}@{}:{}/{}'.format(
    DATABASE, USER, PASSWORD, HOST, PORT, DB_NAME)

DB_CONFIG = {
    "connections": {
        "default": DATABASE_URL,
        "test": "sqlite://:memory:"
    },
    "apps": {
        "models": {
            "models": ["models"],
            "default_connection": environ.get("ENV", "default"),
        }
    }
}
