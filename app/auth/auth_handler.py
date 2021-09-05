import time
from typing import Dict

import jwt
from decouple import config

JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")
JWT_EXPIRY_TIME = config("jwt_expiry_time", default=300.0, cast=float)


def signJWT() -> Dict[str, str]:
    payload = {"user_id": "admin", "expires": time.time() + JWT_EXPIRY_TIME}
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(token)


def token_response(token: str):
    return {"access_token": token}


def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}
