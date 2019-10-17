import dash
import dash_core_components as dcc
import dash_html_components as html
import urllib.parse
from datetime import datetime as dt
import numpy as np
import pandas as pd
import plotly.graph_objs as go

feature_1 = pd.read_excel('time_series_sample_data_1.xlsx')
feature_2 = pd.read_excel('time_series_sample_data_2.xlsx')
dict = {} #dictionary of features
dict["performance"] = feature_1.ffill()
dict["nav"] = feature_2.ffill()





app = dash.Dash(__name__)
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})
app.layout = html.Div([
    html.Div([
        html.H1("Time Series Toolbox"),
    ],
        style={'padding': '50px',
               'backgroundColor': '#3aaab2'}),
    html.P([
                    html.Label("Choose a Fund"),
    dcc.Dropdown(
        id='fund-select',
        options=[
            {'label': 'HF0000001', 'value': 'HF0000001'},
            {'label': 'HF0000002', 'value': 'HF0000002'},
            {'label': 'HF0000003', 'value': 'HF0000003'}

        ],
        value='HF0000001'
    )],
        style = {'width': '400px',
                                    'fontSize' : '20px',
                                    'padding-left' : '100px',
                                    'display': 'inline-block'}),
    html.P([
                    html.Label("Choose a Fund"),
    dcc.Dropdown(
        id='fund-feature',
        options=[
            {'label': 'performance', 'value': 'performance'},
            {'label': 'nav', 'value': 'nav'},
        ],
        value='performance'
    )],
        style = {'width': '400px',
                                    'fontSize' : '20px',
                                    'padding-left' : '100px',
                                    'display': 'inline-block'}),

    html.P([
                    html.Label("Time Period"),
    dcc.DatePickerRange(
        id='my-date-picker-range',
        min_date_allowed=dt(1999, 1, 1),
        max_date_allowed=dt(1999, 4, 29),
        initial_visible_month=dt(1999, 1, 1),
        end_date=dt(1999, 4, 29)
    )],
        style = {'width' : '400px',
                                    'fontSize' : '20px',
                                    'padding-left' : '100px',
                                    'display': 'inline-block'}),
    html.P([
    html.A(
        'Download Data',
        id='download-link',
        download="rawdata.csv",
        href="",
        target="_blank"
    )],
        style = {'width' : '400px',
                                    'fontSize' : '20px',
                                    'padding-left' : '100px',
                                    'display': 'inline-block'}),
    dcc.Graph(id = 'plot')
])


def filter_data(fund, feature,d1=None,d2=None):
    df = dict[feature]
    fund_ts = df.loc[df['fund_id'] == fund]
    fund_ts["date"] = pd.to_datetime(fund_ts["date"])
    if d1 is None:
        return fund_ts.loc[fund_ts['date'] <= d2]
    else:
        return fund_ts.loc[(fund_ts['date'] >= d1) & (fund_ts['date'] <= d2)]


@app.callback(
    dash.dependencies.Output('download-link', 'href'),
    [dash.dependencies.Input('my-date-picker-range', 'start_date'),
     dash.dependencies.Input('my-date-picker-range', 'end_date'),
     dash.dependencies.Input('fund-select', 'value'),
     dash.dependencies.Input('fund-feature', 'value')])
def update_download(start_date, end_date,fund, feature):
    dff = filter_data(fund,feature,start_date,end_date)
    csv_string = dff.to_csv(index=False, encoding='utf-8')
    csv_string = "data:text/csv;charset=utf-8," + urllib.parse.quote(csv_string)
    return csv_string

@app.callback(dash.dependencies.Output('plot', 'figure'),
              [dash.dependencies.Input('my-date-picker-range', 'start_date'),
               dash.dependencies.Input('my-date-picker-range', 'end_date'),
               dash.dependencies.Input('fund-select', 'value'),
               dash.dependencies.Input('fund-feature', 'value')])
def update_figure(start_date, end_date, fund, feature):
    # filtering the data
    dff = filter_data(fund, feature,start_date,end_date)
    # updating the plot
    trace_1 = go.Scatter(x = dff['date'], y = dff[feature],
                        name = 'feature'
                        )
    layout = go.Layout(title='Time Series Plot',
                       hovermode='closest')
    fig = go.Figure(data = [trace_1], layout = layout)
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)