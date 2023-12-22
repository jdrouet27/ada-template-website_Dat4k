import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import time

app = dash.Dash(__name__)

# Layout de l'application
app.layout = html.Div([
    html.Div(id='output-container', style={'margin-top': 20, 'font-size': 24}),
    dcc.Interval(
        id='interval-component',
        interval=1000,  # en millisecondes, mettez à jour toutes les secondes
        n_intervals=0
    ),
])

# Données initiales
countdown_value = 5

# Fonction de mise à jour appelée à chaque intervalle
@app.callback(
    Output('output-container', 'children'),
    [Input('interval-component', 'n_intervals')]
)
def update_layout(n_intervals):
    global countdown_value

    if countdown_value > 0:
        countdown_value -= 1

    # Mise à jour du texte dans la div
    output_text = f"La valeur sera révélée dans {countdown_value} secondes."

    # Si le compte à rebours est terminé, affichez la valeur finale
    if countdown_value == 0:
        output_text = "La valeur est : 27"

    return output_text

if __name__ == '__main__':
    app.run_server(debug=True, port=8051)
