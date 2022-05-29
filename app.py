from setup import app, html, dcc, Output, Input

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