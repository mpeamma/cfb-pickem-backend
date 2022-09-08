from google.oauth2 import id_token
from google.auth.transport import requests

def validate_token(token):
    # Specify the CLIENT_ID of the app that accesses the backend:
    idinfo = id_token.verify_oauth2_token(token,
        requests.Request(),
        '146383021720-j6k5autjeil2c4b6oac4kjhv7gjb70tk.apps.googleusercontent.com')

    # ID token is valid. Get the user's Google Account ID from the decoded token.
    return idinfo
