import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
from datetime import datetime
import pandas as pd

# Set the app
app = dash.Dash()

# Create div to house app.layout
app.layout = html.Div([
    # Div1 to hold header
    html.Div([
        # Div 1.1 to hold stat1
        html.Div([]),
        # Div 1.2 to hold stat2
        html.Div([])
    ]),
    # Div 2 to hold left side bar
    html.Div([
        # Div 2.1 to hold upload button
        html.Div([]),
        # Div 2.2 to hold dropdown
        html.Div([])
    ]),
    # Div 3 to hold graph object
    html.Div([
        dcc.Graph(
            id='plot',
            # input data here with go
            figure={}
        )
    ])  
])
## FUNCTIONS ##
## Abstract these into another file if time permits.

# Function for button action 

# Upload file function

# Function to display stats

if __name__ == "__main_":
    app.run_server()