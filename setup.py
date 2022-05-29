from dash import Dash, html, dcc, Input, Output
import os, dash_auth
from dotenv import load_dotenv
load_dotenv()
app = Dash(__name__)
server = app.server
AUTH_USER = os.environ["AUTH_USER"]
AUTH_PASS = os.environ["AUTH_PASS"]
VALID_USERNAME_PASSWORD_PAIRS = {
    AUTH_USER: AUTH_PASS
}
auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)