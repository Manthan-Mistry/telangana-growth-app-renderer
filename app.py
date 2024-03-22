
import dash
from dash import Dash
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

from src.navbar import navbar



app = Dash(__name__, external_stylesheets = [dbc.themes.BOOTSTRAP,dbc.icons.BOOTSTRAP],
           suppress_callback_exceptions = True, use_pages = True)
server = app.server

navbar = navbar

app.layout = html.Div([
    navbar,
    dash.page_container
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
