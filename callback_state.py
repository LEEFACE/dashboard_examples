import dash
from dash import dcc
from dash import html
from dash.dependencies import Input,Output,State

app = dash.Dash()

app.layout = html.Div([
    dcc.Input(id='number-in',value=1,style={'fontSize':24}),
    html.Button(id='submit-button',
                n_clicks=0,
                children='Submit Here',
                style={'fontSize':24}),
    html.H1(id='number-out')

])

@app.callback(Output('number-out','children'),
            [Input('submit-button','n_clicks')],
            [State('number-in','value')]) #The state is where you're storing it until the Input button is clicked
def output(n_clicks,number):
    return "{} was typed in, and button was clicked {} times".format(number,n_clicks)

if __name__ == '__main__':
    app.run_server()
