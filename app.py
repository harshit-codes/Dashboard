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

app.layout = html.Div([
    html.H2('Hello World'),
    dcc.Dropdown(['BLR', 'BSB', 'BGP'],
        'LA',
        id='dropdown'
    ),
    html.Div(id='display-value')
])

@app.callback(Output('display-value', 'children'),
                [Input('dropdown', 'value')])
def display_value(value):
    return f'Your location is {value}'

if __name__ == '__main__':
    app.run_server(debug=True)