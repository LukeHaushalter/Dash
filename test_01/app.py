# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div( children = [
    html.H1('This is a Dash app.'),
    dcc.Dropdown(
        options=[
            {'label':'Hi', 'value':'Hi'},
            {'label':'Hello', 'value':'Hello'},
            {'label':'What\'s up?','value':'What\'s up?'}
        ]
    )]
)
if __name__ == '__main__':
    app.run_server(debug=True)