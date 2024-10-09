import pandas as pd
import numpy as np
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Creazione di un'app Dash
app = dash.Dash(__name__)

# Dati fittizi per il progetto
np.random.seed(42) # Per avere risultati ripetibili
date_range = pd.date_range(start='2023-01-01', periods=100)
data = {
'Date': date_range,
'Stock Price': np.random.normal(loc=100, scale=10, size=len(date_range)),
'Volume': np.random.randint(100, 1000, size=len(date_range))
}

# Creazione di un DataFrame Pandas
df = pd.DataFrame(data)

# Layout della Dashboard
app.layout = html.Div([
html.H1("Dashboard di Analisi Finanziaria"),
dcc.Graph(id='stock-price-graph'),
dcc.Slider(
id='date-slider',
min=0,
max=len(df) - 1,
value=len(df) - 1,
marks={i: str(df['Date'].iloc[i].date()) for i in range(0, len(df), 10)},
step=1
)
])

# Callback per aggiornare il grafico in base al valore dello slider
@app.callback(
Output('stock-price-graph', 'figure'),
[Input('date-slider', 'value')]
)
def update_graph(selected_index):
    filtered_df = df.iloc[:selected_index+1]
    fig = px.line(filtered_df, x='Date', y='Stock Price', title='Andamento del Prezzo delle Azioni')
    return fig

# Esecuzione dell'app
if __name__ == '__main__':
   app.run_server(debug=True)
