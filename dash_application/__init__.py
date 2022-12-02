import datetime

import dash
from dash import dcc, Input, Output
from dash import html, dash_table

import dash_bootstrap_components as dbc
# from flask_login.utils import login_required
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

from dash_bootstrap_templates import load_figure_template




# select the Bootstrap stylesheet2 and figure template2 for the theme toggle here:
# template_theme1 = "sketchy"
template_theme1 = "flatly"
template_theme2 = "darkly"
# url_theme1 = dbc.themes.SKETCHY
url_theme1 = dbc.themes.FLATLY
url_theme2 = dbc.themes.DARKLY

available_graph_templates: ['ggplot2', 'seaborn', 'simple_white', 'plotly', 'plotly_white', 'plotly_dark',
                            'presentation', 'xgridoff', 'ygridoff', 'gridon', 'none']

templates = [
    "bootstrap",
    "minty",
    "pulse",
    "flatly",
    "quartz",
    "cyborg",
    "darkly",
    "vapor",
]

load_figure_template(templates)

########## DATA_FILES ##############

df_local = pd.read_csv('./datafiles/next_payments_test_data_2.csv')
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')

# url = 'https://drive.google.com/file/d/1DmH3A7I9eONqE2JZKLCCC_dGd3dmDbLO/view?usp=share_link'
# url = 'https://drive.google.com/file/d/114FNn99SAQQsLB_-l0vItgs1Xj-6RtzQ/view?usp=share_link'
# path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]



def create_dash_application(flask_app):
    # dash_app = dash.Dash(server=flask_app, name="Dashboard", url_base_pathname="/dash/", external_stylesheets=[dbc.themes.CERULEAN])
    # server = dash_app.server
    dbc_css = (
        "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.1/dbc.min.css"
    )
    dash_app = dash.Dash(server=flask_app, name="Dashboard", url_base_pathname="/", external_stylesheets=[url_theme1, dbc_css])


    dash_app.layout = html.Div(
        dbc.Container(

            [html.Div(style={'paddingLeft': '15px', 'paddingRight': '20px', 'paddingTop': '5px', 'paddingBottom': '5px',
                             # 'color': 'white'
                             },
                      children=[
                          # укладываем на всю ширину ряда заголовок
                          dbc.Row([
                              dbc.Col(
                                  children=[
                                      html.H3('Интерактивный дашборд'),
                                      dcc.Dropdown(

                                          options=['1', '2', '3'],
                                          multi=True,
                                          # placeholder="Продукт...",
                                          id='input_select',
                                          optionHeight=50,
                                      ),
                                      dash_table.DataTable(
                                          id='activity_status_table',
                                          data=df.to_dict('records'),
                                          columns=[{"name": i, "id": i} for i in df.columns],
                                          style_table={
                                               # 'height': '600px',
                                               'overflowX': 'auto',
                                               'overflowY': 'auto'},
                                           filter_action='native',
                                           sort_action="native",
                                           fixed_rows={
                                               "headers": True,
                                           },
                                          style_header={
                                               'backgroundColor': 'rgb(210, 230, 230)',
                                               'color': 'black',
                                               'fontWeight': 'bold'
                                           },
                                          style_data={
                                           'whiteSpace': 'normal',
                                           'height': 'auto'},
                                                       style_cell={
                                                           'minWidth': '180px', 'width': '180px',
                                                           'maxWidth': '180px',
                                                           'whiteSpace': 'normal',
                                                           'textOverflow': 'ellipsis',
                                                           'overflow': 'hidden'
                                                       },
                                                           export_format="csv"
                                                           ),

                                  ]
                              )
                          ]),


                      ]
                      ),
             ],


            fluid=True,
            className="dbc"
            # className='custom_container'
        )
    )



    init_callbacks(dash_app)


    return dash_app


def init_callbacks(dash_app):
    @dash_app.callback([Output('activity_status_table', 'data'),
                       ],
                      [
                          Input('input_select', 'value'),
                      ])

    def deals_tab():
        data = df

        return [data]