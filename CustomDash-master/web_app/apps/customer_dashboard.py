import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from web_app.app import app
from web_app.apps.helpers.helper_functions import get_extended_values, get_location, get_gender, \
                                                  get_age, get_segment, get_churn

import pandas as pd

df = pd.read_csv(r"C:\Users\LENOVO\Desktop\CustomDash-master\web_app\appdata\blogdata.csv")

COLUMNS = list(df.columns)

COLORS = {
    'background': '#28283c',
    'text': '#77d1d6',
}

apparel_id = 1
MONTHS = ['August', 'September', 'October', 'November', 'December', 'January']


def generate_arpu_graph(apparel):
    return {
        'data': [
            {
                'x': MONTHS,
                'y': get_extended_values(df.iloc[apparel]['Croptop']),
                'type': 'bar',
                'marker': {
                    'color': '#63b7af',
                    'size': 10,
                },
                'width': [0.4] * 6,
            },
        ],
        'layout': {
            'title': 'Average search appearance',
            'showlegend': False,
            'colorscale': 'balance',
            'legend': {
                'x': 0,
                'y': 1.0
            },
            'plot_bgcolor': COLORS['background'],
            'paper_bgcolor': COLORS['background'],
            'font': {
                'color': COLORS['text']
            },
            'transition': {
                'duration': 1500
            },
            'yaxis': {
                'range': [0, 1200]
            },
        }
    }


def generate_service_usage_graph(apparel):
    return {
        'data': [
            {
                'x': MONTHS,
                'y': get_extended_values(df.iloc[apparel]['Pencil Skirt']),
                'name': 'Pencil Skirt',
                'marker': {
                    'color': '#ff9d76',
                    'size': 10,
                }
            },
            {
                'x': MONTHS,
                'y': get_extended_values(df.iloc[apparel]['Miniskirt']),
                'name': 'Miniskirt',
                'marker': {
                    'color': '#a3f7bf',
                    'size': 10,
                }
            },
            {
                'x': MONTHS,
                'y': get_extended_values(df.iloc[apparel]['A-line']),
                'name': 'A-line',
                'marker': {
                    'color': '#05dfd7',
                    'size': 10,
                }
            }
        ],
        'layout': {
            'title': 'Appearances in Blogs',
            'showlegend': False,
            'colorscale': 'balance',
            'legend': {
                'x': 0,
                'y': 1.0
            },
            'plot_bgcolor': COLORS['background'],
            'paper_bgcolor': COLORS['background'],
            'font': {
                'color': COLORS['text']
            },
            'transition': {
                'duration': 1500
            },
            'yaxis': {
                'range': [0, 1200]
            },
        }
    }


def generate_search_probability(apparel):
    return html.Div(
        id='Number of searches',
        children=str(df.iloc[apparel]['Number of searches']) + "%"
    )


# df = pd.read_csv(r"C:\Users\LENOVO\Desktop\CustomDash-master\web_app\appdata\blogdata.csv")

layout = html.Div([
    html.Div([
        html.Div([
            html.H3(
                html.Strong(
                    '''
                    CUSTOMDASH
                    ''', id='customdash'),
            ),
            html.Div([
                dcc.Input(
                    id='apparel-id',
                    type='Number',
                    placeholder='Enter apparel ID...',
                    value=1,
                    className='eight columns'
                ),
                html.Button('Submit', id='submit-button', className='four columns'),
            ], className='container', style={'width': '100%'})
        ], className='six columns'),

        html.Div([
            html.P([
                html.Strong('apparel Name :  ', className='info-title'),
                html.Strong('Skirt', id='display-apparel-id', className='info-value'),
            ], className='text-apparel-id'),
            html.P([
                html.Strong('Trending Keyword :  ', className='info-title'),
                html.Strong('Pencil Skirt', className='info-value', id='location'),
            ], className='text-apparel-id'),
            html.P([
                html.Strong('Date :  ', className='info-title'),
                html.Strong('7-08-2020', className='info-value', id='age'),
            ], className='text-apparel-id'),
            html.P([
                html.Strong('Most Rising Searches :  ', className='info-title'),
                html.Strong('Nike Tennis Skirt', className='info-value', id='gender'),
            ], className='text-apparel-id'),
        ], className='six columns container', id='apparel-info')
    ], className='container'),

    html.Div([
        html.Div([
            dcc.Graph(
                id='Croptop-graph',
                style={'width': '100%'},
                figure=generate_arpu_graph(apparel_id))
        ], className='six columns', style={'width': '48%'}),

        html.Div([
            dcc.Graph(
                id='service-usage-graph',
                figure=generate_service_usage_graph(apparel_id)),
        ], className='six columns'),

    ], className='container'),

    html.Div([
        html.Div([
            html.Div([
                html.Strong('TREND', className='titles'),
                generate_search_probability(1)
            ], className='six columns', id='display-apparel-churn'),
            html.Div([
                html.Strong('Blog Referred', className='titles'),
                html.Div([
                    get_segment(apparel_id)
                ], id='apparel-segment')
            ], className='six columns', id='display-apparel-segment')
        ], className='container'),
    ], id='last-div'),

    html.Div([
        html.Button([
            dcc.Link('ANALYTICS DASHBOARD', href='/apps/overall_dashboard')
        ], id='page2-link', className='three columns'),
    ], className='container', id='page2-link-container')

])


@app.callback(
    [Output('display-apparel-id', 'children'),
     Output('location', 'children'),
     Output('age', 'children'),
     Output('gender', 'children')],
    [Input('submit-button', 'n_clicks')],
    [State('apparel-id', 'value')],
)
def update_customer_id(n_clicks, value):
    return value, get_location(value), get_age(value), get_gender(value)


@app.callback(
    Output('service-usage-graph', 'figure'),
    [Input('submit-button', 'n_clicks')],
    [State('apparel-id', 'value')]
)
def service_usage_graph(n_clicks, value):
    return generate_service_usage_graph(value)


@app.callback(
    Output('Croptop-graph', 'figure'),
    [Input('submit-button', 'n_clicks')],
    [State('apparel-id', 'value')]
)
def update_search_graph(n_clicks, value):
    return generate_arpu_graph(value)


@app.callback(
    Output('Number of searches', 'children'),
    [Input('submit-button', 'n_clicks')],
    [State('apparel-id', 'value')]
)
def update_churn_probability(n_clicks, value):
    return get_churn(value)


@app.callback(
    Output('apparel-segment', 'children'),
    [Input('submit-button', 'n_clicks')],
    [State('apparel-id', 'value')]
)
def update_customer_segment(n_clicks, value):
    return get_segment(value)
