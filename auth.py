# auth.py

import os
import jwt
from functools import wraps
from flask import request, g, abort

JWT_SECRET = os.getenv("JWT_SECRET")

def jwt_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        auth = request.headers.get("Authorization", "")
        token = auth.replace("Bearer ", "")
        if not token:
            abort(401, "Missing JWT")
        try:
            payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
            g.user_id = payload["sub"]
            g.user_role = payload.get("role", "guest")
        except jwt.PyJWTError:
            abort(401, "Invalid JWT")
        return f(*args, **kwargs)
    return wrapper

def roles_required(*roles):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if g.user_role not in roles:
                abort(403, "Insufficient role")
            return f(*args, **kwargs)
        return wrapper
    return decorator