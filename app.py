# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

df = pd.read_csv(
    'Data/microfibre_loss_per_clothing_type.csv').groupby(['item_type', 'lint_trap_used'], as_index=False).mean()

fig = px.bar(df,
             x='item_type',
             y='microfibre_loss',
             color='lint_trap_used',
             barmode='group')

app.layout = html.Div(children=[
    html.H1('Microfiber Loss'),

    html.Div(children='''
        Average microfiber loss per textile type.
    '''),
    dcc.Graph(
        id='microfiber-loss-textile',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
