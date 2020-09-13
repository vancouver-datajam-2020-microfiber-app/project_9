# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['./assets/style.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

df = pd.read_csv('Data/microfibre_loss_per_clothing_type.csv')

fig = px.bar(df,
    x='item_type',
    y='avg_microplastic_loss',
    color='lint_trap_used')

app.layout = html.Div(children=[
    html.H1('Know Your Impact'),
    html.Img(src = './assets/img/datajam.jpg',
        height = '100px'
    ),
    html.H1('Microfiber Loss'),
    
    html.H6('Research indicates that home laundry of synthetic textiles are big contributors to microplastics in ocean which are ingested by marine plankton and move across food web. Select the options below to know how you do your laundry impacts ocean health.'),
    
    dcc.Graph(
        id='microfiber-loss-textile',
        figure=fig
    ),
    html.Div(children='''
        Average microfiber loss per textile type.
    ''')
])

if __name__ == '__main__':
    app.run_server(debug=True)
