import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

#declare the app
app = dash.Dash()

app.layout = html.Div ([
    dcc.Input(id='my-id',value='Initial Text', type='text'),
    html.Div(id='my-div')
])

#connect the div and the Input through the use of a callback decorator
@app.callback(Output(component_id='my-div',component_property='children'), 
    [Input(component_id='my-id',component_property='value')])
def update_output_div(input_value):
    return "You entered: {}".format(input_value)

if __name__ == '__main__':
    app.run_server()