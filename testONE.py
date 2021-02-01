import dash
import dash_core_components as dcc
import pandas as pd
import plotly.express as px
import dash_html_components as html
from dash.dependencies import Input, Output

df = pd.read_csv('https://raw.githubusercontent.com/sp4c3j1mm1/csv_monitoramento/main/csv_trafo_fases.csv')

app = dash.Dash(__name__)

app.layout = html.Div([

    html.H1("Monitoramento de Trafos", style={'text-align': 'center'}),
    dcc.Graph(id="graph"),
    #html.Button("Fase", id='btn', n_clicks=0),
    dcc.Dropdown(id="slct_fase",
                 options=[
                     {"label": "Fase A", "value": 'v_faseA'},
                     {"label": "Fase B", "value": 'v_faseB'},
                     {"label": "Fase C", "value": 'v_faseC'}],
                 multi=False,
                 #value=2015,
                 style={'width': "40%"}
                 ),

    html.Div(id='output_container', children=[]),
    html.Br(),
])

@app.callback(
    [Output(component_id='output_container', component_property='children')],
    [Input(component_id='slct_fase', component_property='value')]
)

def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    container = "FASE ESCOLHIDA: {}".format(option_slctd)

    dff = df.copy()
    dff = dff[dff["fase"] == option_slctd]
    # dff = dff[dff["Affected by"] == "Varroa_mites"]


    fig = px.bar(df, x=['1', '2', '3'], y=option_slctd)

    return container, fig

app.run_server(debug=True)

# fig = px.bar(df, x = [1, 2, 3 ], y = 'v_faseA', title='Vai porra')
# fig.show()
