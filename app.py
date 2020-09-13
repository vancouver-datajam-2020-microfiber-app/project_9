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

df = pd.read_csv(
    'Data/microfibre_loss_per_clothing_type.csv').groupby(['item_type', 'lint_trap_used'], as_index=False).mean()

fig = px.bar(df,
             x='item_type',
             y='microfibre_loss',
             color='lint_trap_used',
             barmode='group')

app.layout = html.Div(children=[
    html.H1('Know Your Impact'),
    html.Img(src='./assets/img/datajam.jpg',
             height='100px'
             ),
    html.H1('Microfiber Loss'),

    html.H6('Research indicates that home laundry of synthetic textiles are big contributors to microplastics in ocean which are ingested by marine plankton and move across food web. Select the options below to know how you do your laundry impacts ocean health.'),

    dcc.Graph(
        id='microfiber-loss-textile',
        figure=fig
    ),
    html.Div(children='''
        Average microfiber loss per textile type.
    '''),

    html.H5('Lint Trap '
            ),

    html.Div(children='''
        Install a lint trap on your washing machine to catch microfibres before they make it into the ocean. Lint traps can reduce microfibre out put by up to 87.
    '''),

    html.Img(src='./assets/img/softener.png',
             height='100px'
             ),

    html.H5('Fabric Softener'
            ),

    html.Div(children='''
        Add fabric softener to your wash load to reduce microfibre shedding. Using fabric softener can prevent up to 45% of microfibres from being shed.
    '''),

    html.Img(src='./assets/img/washing_machine.png',
             height='100px'
             ),

    html.H5('Cold Water Wash'
            ),
    html.Div(children='''
        In addition to using less energy, using the cold water cycle is better for your clothes, and reduces microfibre output up to 30% compared to a hot water wash.

    '''),
])

if __name__ == '__main__':
    app.run_server(debug=True)
