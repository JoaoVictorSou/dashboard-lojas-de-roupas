# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

# Biblioteca de dashboard com módulos de componentes layout e callbacks
from dash import Dash, html, dcc
# Biblioteca de construção de gráficos
import plotly.express as px
import pandas as pd

# Criação de um app que servirá como esqueleto para um servidor de dashboard
app = Dash(__name__)

# Dataframe com a base de dados que será consumida pelo Plotly
df = pd.read_excel("./bd/Vendas.xlsx")

# Base de dados em dataframe transformada em gráfico especificando suas respectivas coordenadas
fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")

# Corpo da página dashboard
app.layout = html.Div(children=[
    # Elemento HTML da forma que é reconhecido
    html.H1(children='Dashboard'),

    html.Div(children='''
        Vendas concorrentes no setor de moda
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
