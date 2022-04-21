import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import pandas_datareader.data as web
from datetime import datetime
import pandas as pd

app = dash.Dash()

# VERSION 2 of Ericsson Dashboard

#['trace','date','freq','power','carrier','mean']
erc = pd.read_csv('/Users/leeannewalker/Desktop/App_Stu_Proj/mock_data.csv')
erc.set_index('UUID', inplace=True)
options = []
for tic in erc.index:
    options.append({'label':'{} {}'.format(tic,erc.loc[tic]['date']), 'value':tic})

app.layout = html.Div([
    html.H1('Ericsson Dashboard v2'),
    html.Div([
        html.H3('Select UUID Anomaly:', style={'paddingRight':'30px'}),
        # replace dcc.Input with dcc.Options, set options=options
        dcc.Dropdown(
            id='my_ticker_symbol',
            options=options,
            value=["A"], ## default UUID to start on
            multi=True
        )
    # widen the Div to fit multiple inputs
    ], style={'display':'inline-block', 'verticalAlign':'top', 'width':'30%'}),
    html.Div([
        html.H3('Select start and end dates:'),
        dcc.DatePickerRange(
            id='my_date_picker',
            min_date_allowed=datetime(2022, 1, 1),
            max_date_allowed=datetime.today(),
            start_date=datetime(2022, 1, 1),
            end_date=datetime.today()
        )
    ], style={'display':'inline-block'}),
    html.Div([
        html.Button(
            id='submit-button',
            n_clicks=0,
            children='Submit',
            style={'fontSize':24, 'marginLeft':'30px'}
        ),
    ], style={'display':'inline-block'}),
    dcc.Graph(
        id='my_graph',
        figure={
            'data': [
                {'x': [1,2], 'y': [3,1]} ## default for graph to start on
            ]
        }
    )
])
@app.callback(
    Output('my_graph', 'figure'),
    [Input('submit-button', 'n_clicks')],
    [State('my_ticker_symbol', 'value'),
    State('my_date_picker', 'start_date'),
    State('my_date_picker', 'end_date')])
def update_graph(n_clicks, anomaly_ticker, start_date, end_date) :
    start = datetime.strptime(start_date[:10], '%Y-%m-%d')
    end = datetime.strptime(end_date[:10], '%Y-%m-%d')
    # since anomaly_ticker is now a list of symbols, create a list of traces
    traces = []

    erc = pd.read_csv('/Users/leeannewalker/Desktop/App_Stu_Proj/mock_data.csv')

    for tic in anomaly_ticker:
        mask = erc['UUID'].str.contains(tic)
        filtered_df = erc[mask]
        traces.append({'x':filtered_df['date'], 'y': filtered_df['freq'], 'name':tic})
    fig = {
        # set data equal to traces
        'data': traces,
        # use string formatting to include all symbols in the chart title
        'layout': {'title':', '.join(anomaly_ticker)+' Anomaly detector'}
    }
    return fig

if __name__ == '__main__':
    app.run_server()