import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go
import numpy as np

app = dash.Dash()

#creating test data
np.random.seed(42)
random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

app.layout = html.Div([dcc.Graph(id='scatterplot',
                        figure = {'data':[
                                    go.Scatter(
                                        x=random_x,
                                        y=random_y,
                                        mode='markers',
                                        marker= {
                                            'size':12,
                                            'color':'rgb(51,204,153)',
                                            'symbol':'pentagon',
                                            'line':{'width':2}

                                        }
                                    )],
                                 'layout':go.Layout( title='My Scatter Plot',
                                                    xaxis = {'title':'Some X Title'} 
                                 ) })
                        ])

if __name__ == '__main__':
    app.run_server()