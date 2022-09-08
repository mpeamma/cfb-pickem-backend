from functools import wraps
from flask import abort, request
from config.google_auth import validate_token

def authorize(f):
    @wraps(f)
    def decorated_function(*args, **kws):
        if not 'Authorization' in request.headers:
            abort(401)

        jwt = request.headers.get("Authorization")
        token = str.replace(str(jwt), 'Bearer ','')
        try:
            user = validate_token(token)
        except ValueError:
            abort(401)

        return f(user=user, *args, **kws)
    return decorated_function
