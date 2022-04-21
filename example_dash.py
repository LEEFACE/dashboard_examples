import dash
from dash import dcc
from dash import html

#create the application, the dashboard itself
app = dash.Dash()

# Create a colours dictionary
# a good way to have a central source of truth and ability to quick change styling
colours = {'background':'#111111', 'text':'#7FDBFF'}


app.layout = html.Div(children=[
    html.H1('Hello Dash',style={'textAlign':'center',
                                'color':colours['text']}),
    dcc.Graph(id='example',
                figure={'data':[
                    {'x':[1,2,3],'y':[4,1,2],'type':'bar','name':'SF'},
                    {'x':[1,2,3],'y':[2,4,5],'type':'bar','name':'nyc'}
                    ],
                         'layout':{
                             'plot_bgcolor':colours['background'],
                             'paper_bgcolor':colours['background'],
                             'font':{'color':colours['text']},
                             'title':'BAR PLOTS!'
                         }})
], style={'backgroundColor':colours['background']}

)

#checks to see if you're calling this script directly (i.e. cd'd to this directory)
if __name__ == '__main__':
    app.run_server()