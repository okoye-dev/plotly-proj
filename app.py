from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('sales-data.csv')

app = Dash()
print(df.head(10))

app.layout = [
    html.H1(children='Qing and Orpen Sales Data', style={'textAlign':'center'}),
]

if __name__ == '__main__':
    app.run(debug=True)
