# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

# Biblioteca de dashboard com módulos de componentes layout e callbacks
from dash import Dash, html, dcc, Output, Input
# Biblioteca de construção de gráficos
import plotly.express as px
import pandas as pd

# Criação de um app que servirá como esqueleto para um servidor de dashboard
app = Dash(__name__)

# Dataframe com a base de dados que será consumida pelo Plotly
df = pd.read_excel("./bd/Vendas.xlsx")
fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")

options = list(df["ID Loja"].unique())
options.append("Todas as lojas")

# Corpo da página dashboard
app.layout = html.Div(children=[
    # Elemento HTML da forma que é reconhecido
    html.H1(children='Dashboard'),
    html.Div(children='''
        Vendas das filiais no setor de moda
    '''),
    dcc.Dropdown(options, value = "Todas as lojas", id = "clothes-options"),
    dcc.Graph(
        id='sales-quantity-chart',
        figure= fig
    )
])

"""
O decorator indica qual é o DCC de entreda (que define o dado) e o de saída (que mostra os dados)
"""
@app.callback(
    Output("sales-quantity-chart", "figure"),
    Input("clothes-options", "value")

)
def update_output(value):
    if value == "Todas as lojas":
        # Base de dados em dataframe transformada em gráfico especificando suas respectivas coordenadas
        fig_selected = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
    else:
        filtered_table = df.loc[df['ID Loja'] == value, :] 
        fig_selected = px.bar(filtered_table, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
    
    return fig_selected

if __name__ == '__main__':
    app.run_server(debug=True)
