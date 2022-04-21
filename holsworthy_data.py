#######
# This makes a 3x3 scatterplot of wheels.csv, and sends
# the results of a selection to the screen as a JSON object.
######
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import numpy as np

app = dash.Dash()

df = pd.read_csv('/Users/leeannewalker/HOUSE_PROJ_V1/raw_holsworthy_data.csv')

df['settlement_date'] = pd.to_datetime(df['settlement_date'], format='%Y%m%d').dt.strftime('%d/%m/%Y')
df = df.sort_values(by=['download_timestamp'],ascending=True)


app.layout = html.Div([
    html.Div([
        dcc.Graph(id='plot',
            figure={'data':[go.Scatter(
            x=df['download_timestamp'],
            y=df['purchase_price'],
            mode='markers'
        )],
                'layout':go.Layout(title='Scatterplot',hovermode='closest')})
        ], style={'width':'90%','height':'70%','display':'inline-block'}),
    
    
    html.Div([
        dcc.Markdown(id='house_stats')
    ],style={'width':'20%','height':'50%','display':'inline-block'})

])

#return information in json
@app.callback(Output('house_stats','children'),
    [Input('plot','hoverData')])
def callback_stats(hoverData):
    v_index = hoverData['points'][0]['pointIndex']
    stats = """
            Address: {} {} \n
            Purchase price: ${} \n
            Settlement date: {}
            """.format(df.iloc[v_index]['property_house_number'],
                       df.iloc[v_index]['property_street_name'],
                       df.iloc[v_index]['purchase_price'],
                       df.iloc[v_index]['settlement_date'])
    return stats

if __name__ == '__main__':
    app.run_server()