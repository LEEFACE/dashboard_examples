import dash
from dash import dcc
from dash import html
from dash.dependencies import Input,Output
import plotly.graph_objects as go
import pandas as pd
import json
import base64

app = dash.Dash()

df = pd.read_csv('/Users/leeannewalker/Plotly-Dashboards-with-Dash/Data/wheels.csv')

def encode_image(image_file):
    encoded = base64.b64encode(open(image_file, 'rb').read())
    return 'data:image/png;base64,{}'.format(encoded.decode())

app.layout = html.Div([
    html.Div(dcc.Graph(id='wheels-plot',
                        figure={'data':[go.Scatter(
                            x=df['color'],
                            y=df['wheels'],
                            dy = 1, # to space it out a bit
                            mode='markers',
                            marker={'size':15}
            )],
            'layout':go.Layout(title='Test',hovermode='closest')}
            ),style={'width':'30%','float':'left'}),
    html.Div([html.Img(id='hover-data',src='children',height=300)], 
    style={'paddingTop':35}),
])

@app.callback(Output('hover-data','src'),
            [Input('wheels-plot','hoverData')]) # hoverData is a property that belongs to any dcc graph, so you don't need to decalre it, it's already there
def callback_image(hoverData):
    wheel=hoverData['points'][0]['y']
    color=hoverData['points'][0]['x']
    path='/Users/leeannewalker/Plotly-Dashboards-with-Dash/Data/images/'
    return encode_image(path+df[(df['wheels']==wheel) & (df['color']==color)]['image'].values[0])

if __name__ == "__main__":
    app.run_server()