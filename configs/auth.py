from os import environ


AUTH_SECRET_KEY = str(environ.get("AUTH_SECRET_KEY"))
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = float(
    str(environ.get("ACCESS_TOKEN_EXPIRE_MINUTES")))
