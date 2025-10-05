from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.data as pldata

df = pldata.gapminder(return_type='pandas')

# Initialize Dash app
app = Dash(__name__)
server = app.server

countries = df.drop_duplicates(subset=['country'], keep='first')['country']

# Layout
app.layout = html.Div([
    dcc.Dropdown(
        id="country-dropdown",
        options=[{"label": country, "value": country} for country in countries],
        value="Canada"
    ),
    dcc.Graph(id="gdp-growth")
])

# Callback for dynamic updates
@app.callback(
    Output("gdp-growth", "figure"),
    [Input("country-dropdown", "value")]
)
def update_graph(country):
    fig = px.line(df, x="year", y="gdpPercap", title=f"{country}")
    return fig

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
